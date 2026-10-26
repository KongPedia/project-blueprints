"""Native Copier post-copy provisioning, with a recording CLI instead of personal host mutations."""

import json
import os
import shutil
import sys

from copier import run_copy, run_update
from copier.errors import TaskError, UnsafeTemplateError
from plumbum import local
import pytest

from helpers import MARKET, PROFILE_PLUGINS, assert_selection, git


@pytest.fixture
def codex_calls(tmp_path):
    executable = tmp_path / "tools/codex"
    executable.parent.mkdir()
    executable.write_text(f"#!{sys.executable}\n" + '''import json, os, sys
from pathlib import Path
with Path(os.environ["CODEX_CALL_LOG"]).open("a") as stream:
    stream.write(json.dumps({"args": sys.argv[1:], "cwd": os.getcwd()}) + "\\n")
if sys.argv[3].split("@")[0] == os.environ.get("FAIL_PLUGIN"):
    print("Native fixture install failure", file=sys.stderr)
    sys.exit(23)
''')
    executable.chmod(0o755)
    log = tmp_path / "codex-calls.jsonl"

    def read():
        return [json.loads(line) for line in log.read_text().splitlines()] if log.exists() else []

    home = tmp_path / "host-home"
    codex_home = tmp_path / "codex-home"
    home.mkdir()
    codex_home.mkdir()
    # Copier exports plumbum's environment, not a fresh os.environ snapshot.
    with local.env(PATH=str(executable.parent) + os.pathsep + os.environ["PATH"],
                   CODEX_CALL_LOG=str(log), HOME=str(home), CODEX_HOME=str(codex_home), FAIL_PLUGIN=""):
        yield read


@pytest.mark.parametrize(("answers", "expected"), [
    ({"profile": "python"}, PROFILE_PLUGINS["python"]),
    ({"profile": "nextjs"}, PROFILE_PLUGINS["nextjs"]),
    ({"layout": "monorepo", "monorepo_preset": "python-web"},
     PROFILE_PLUGINS["python-fastapi"] | PROFILE_PLUGINS["react-typescript"]),
])
def test_trusted_copy_installs_only_the_selected_codex_union(template_source, tmp_path, codex_calls, answers, expected):
    project = tmp_path / "consumer"
    run_copy(str(template_source), project, data={"project_name": "consumer", **answers},
             defaults=True, quiet=True, unsafe=True, skip_tasks=False)
    assert [entry["args"] for entry in codex_calls()] == [
        ["plugin", "add", f"{name}@{MARKET}"] for name in sorted(expected)
    ]
    assert all(entry["cwd"] == str(project.resolve()) for entry in codex_calls())
    assert_selection(project, expected)


def test_explicit_source_is_refused_before_any_host_install(template_source, tmp_path, codex_calls):
    with pytest.raises(TaskError):
        run_copy(str(template_source), tmp_path / "consumer", data={"project_name": "consumer",
                 "agent_skills_repository": "Example-Team/agent-skills", "agent_skills_ref": "v0.2.0"},
                 defaults=True, quiet=True, unsafe=True, skip_tasks=False)
    assert not codex_calls(), "Never silently install a different host snapshot for an explicit Git source"


def test_untrusted_template_refuses_execution_and_skip_tasks_is_render_only(template_source, tmp_path, codex_calls):
    with pytest.raises(UnsafeTemplateError):
        run_copy(str(template_source), tmp_path / "untrusted", data={"project_name": "consumer"},
                 defaults=True, quiet=True, unsafe=False, skip_tasks=False)
    assert not codex_calls()
    project = tmp_path / "render-only"
    run_copy(str(template_source), project, data={"project_name": "consumer"},
             defaults=True, quiet=True, unsafe=False, skip_tasks=True)
    assert not codex_calls()
    assert_selection(project, PROFILE_PLUGINS["python"])


@pytest.mark.parametrize("failed_plugin", ["common", "python"])
def test_install_failure_stops_instead_of_reporting_a_provisioned_project(
    template_source, tmp_path, codex_calls, monkeypatch, capfd, failed_plugin,
):
    monkeypatch.setitem(local.env, "FAIL_PLUGIN", failed_plugin)
    with pytest.raises(TaskError):
        run_copy(str(template_source), tmp_path / "consumer", data={"project_name": "consumer"},
                 defaults=True, quiet=True, unsafe=True, skip_tasks=False)
    attempted = ["common"] if failed_plugin == "common" else ["common", "python"]
    assert [entry["args"] for entry in codex_calls()] == [
        ["plugin", "add", f"{name}@{MARKET}"] for name in attempted
    ], "Stop without uninstalling previously added host plugins"
    stderr = capfd.readouterr().err
    assert "Native fixture install failure" in stderr
    assert "codex plugin marketplace add" in stderr, "Failed setup must show the one-time registration remedy"
    assert "Traceback" not in stderr


def test_missing_codex_shows_actionable_recovery_without_host_changes(
    template_source, tmp_path, codex_calls, monkeypatch, capfd,
):
    empty_path = tmp_path / "no-tools"
    empty_path.mkdir()
    monkeypatch.setitem(local.env, "PATH", str(empty_path))
    with pytest.raises(TaskError):
        run_copy(str(template_source), tmp_path / "consumer", data={"project_name": "consumer"},
                 defaults=True, quiet=True, unsafe=True, skip_tasks=False)
    assert not codex_calls()
    stderr = capfd.readouterr().err
    assert "Codex CLI" in stderr and "--skip-tasks" in stderr
    assert "Traceback" not in stderr


def test_guidance_adoption_and_updates_do_not_install_plugins(template_source, tmp_path, codex_calls):
    run_copy(str(template_source), tmp_path / "adoption", data={"project_name": "consumer", "adoption": "guidance"},
             defaults=True, quiet=True, unsafe=True, skip_tasks=False)
    assert not codex_calls()
    source = tmp_path / "versioned-source"
    shutil.copytree(template_source, source, symlinks=True)
    git(source, "init", "--template=", "-b", "main")
    git(source, "add", ".")
    git(source, "commit", "-m", "Disposable reviewed task source")
    git(source, "tag", "v1.0.0")
    project = tmp_path / "consumer"
    run_copy(str(source), project, vcs_ref="v1.0.0", data={"project_name": "consumer"},
             defaults=True, quiet=True, unsafe=True, skip_tasks=False)
    before = codex_calls()
    assert len(before) == 2
    git(project, "init", "--template=", "-b", "main")
    git(project, "add", ".")
    git(project, "commit", "-m", "Disposable enrolled consumer")
    guidance = source / "template/.agents/README.md.jinja"
    guidance.write_text(guidance.read_text() + "\nReviewed guidance update.\n")
    git(source, "add", ".")
    git(source, "commit", "-m", "Disposable guidance-only revision")
    git(source, "tag", "v2.0.0")
    run_update(project, vcs_ref="v2.0.0", defaults=True, quiet=True, overwrite=True, unsafe=True, skip_tasks=False)
    assert codex_calls() == before
    assert "Reviewed guidance update." in (project / ".agents/README.md").read_text()
