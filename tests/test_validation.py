"""Trust-boundary validation must fail before producing target files."""

import json
import os
import re
import shutil
import subprocess
import sys

from copier.errors import UserMessageError
import pytest

from helpers import configs, render


@pytest.mark.parametrize("data", [
    {"project_name": "../escape"}, {"project_name": "bad;name"}, {"project_name": "async"},
    {"project_name": "a" * 64}, {"profile": "unknown"},
    {"profile": "python-fastapi", "project_name": "fastapi"},
    {"profile": "python-litestar", "project_name": "httpx"},
    {"profile": "rust", "project_name": "test"}, {"profile": "rust", "project_name": "build"},
    {"agent_skills_repository": "https://github.com/org/repo"},
    {"agent_skills_repository": "user:secret@github.com/org/repo"},
    {"agent_skills_repository": "org/repo;touch PWNED"},
    {"agent_skills_repository": "org/../repo"}, {"agent_skills_repository": "org/repo\n"},
    {"agent_skills_ref": "--upload-pack=evil"}, {"agent_skills_ref": "$(touch PWNED)"},
    {"agent_skills_ref": "refs/../main"}, {"agent_skills_ref": "branch\n"},
    {"layout": "monorepo", "monorepo_preset": "unknown"},
    {"layout": "monorepo", "components": [{"name": "../escape", "kind": "apps", "profile": "python"}]},
    {"layout": "monorepo", "components": [{"name": "api", "kind": "other", "profile": "python"}]},
    {"layout": "monorepo", "components": [{"name": "api", "kind": "apps", "profile": "unknown"}]},
    {"layout": "monorepo", "components": [
        {"name": "same", "kind": "apps", "profile": "python"},
        {"name": "same", "kind": "packages", "profile": "rust"}]},
    {"layout": "monorepo", "components": [{"name": "api", "kind": "apps", "profile": "python", "path": "/tmp"}]},
    {"selected_plugins": ["session-guidance"]}, {"known_plugins": []}, {"registry": {}}, {"packages": []},
    {"agent_delivery": "local"}, {"agent_delivery_baseline": "plugins"}, {"rust_async": True},
])
def test_invalid_or_obsolete_inputs_are_rejected_before_output(template_source, tmp_path, data):
    project = tmp_path / "consumer"
    with pytest.raises((ValueError, UserMessageError)):
        render(template_source, project, **data)
    assert not project.exists() or not list(project.rglob("*"))


def test_advanced_safe_source_revision_is_shared_by_both_hosts(template_source, tmp_path):
    from helpers import MARKET

    project = tmp_path / "consumer"
    render(template_source, project, agent_skills_repository="My-Org/agent-skills", agent_skills_ref="release/v1.2.3")
    codex, claude = configs(project)
    assert codex["marketplaces"][MARKET]["source"] == "https://github.com/My-Org/agent-skills.git"
    assert codex["marketplaces"][MARKET]["ref"] == "release/v1.2.3"
    assert claude["extraKnownMarketplaces"][MARKET]["source"]["ref"] == "release/v1.2.3"


@pytest.mark.parametrize("profile", ["python", "python-fastapi", "python-litestar"])
@pytest.mark.parametrize("layout", ["single", "monorepo"])
@pytest.mark.parametrize("name", ["email", "typing", "json", "msvcrt", "aifc", "tomllib", "annotationlib", "py-compile"])
def test_python_profiles_reject_stdlib_module_collisions_before_output(
    template_source, tmp_path, profile, layout, name,
):
    project = tmp_path / "consumer"
    data = {"profile": profile, "project_name": name} if layout == "single" else {
        "layout": "monorepo", "components": [{"name": name, "kind": "packages", "profile": profile}],
    }
    with pytest.raises((ValueError, UserMessageError), match="standard library"):
        render(template_source, project, **data)
    assert not project.exists() or not list(project.rglob("*"))


def test_stdlib_registry_covers_the_running_python_without_platform_filtering(template_source):
    registry = json.loads((template_source / "blueprints/profiles.json").read_text())
    names = set(registry.get("python_stdlib", {}).get("module_names", []))
    accepted_modules = {name for name in sys.stdlib_module_names if re.fullmatch(r"[a-z][a-z0-9_]*", name)}
    assert accepted_modules <= names, f"Refresh the reviewed stdlib registry for Python {sys.version}: {sorted(accepted_modules - names)}"


@pytest.mark.parametrize("profile", ["react-typescript", "nestjs", "nextjs", "rust", "cpp-firmware"])
@pytest.mark.parametrize("layout", ["single", "monorepo"])
def test_non_python_profiles_allow_names_used_by_python_stdlib(template_source, tmp_path, profile, layout):
    project = tmp_path / "consumer"
    data = {"project_name": "email", "profile": profile} if layout == "single" else {
        "layout": "monorepo", "components": [{"name": "py-compile", "kind": "packages", "profile": profile}],
    }
    render(template_source, project, **data)
    assert (project / "README.md").is_file()


@pytest.mark.parametrize("broken_boundary", [None, "foreign-package", "module-entrypoint"])
def test_generated_python_smoke_checks_owned_package_and_executed_entrypoint(
    rendered_profile, tmp_path, broken_boundary,
):
    project = tmp_path / "consumer"
    shutil.copytree(rendered_profile("python"), project)
    import_root = project / "src"
    if broken_boundary == "foreign-package":
        # The old import-only smoke accepts an unrelated package with the same import name.
        import_root = tmp_path / "unrelated"
        package = import_root / "sample_project"
        package.mkdir(parents=True)
        (package / "__init__.py").write_text("# Not owned by this scaffold.\n")
        (package / "__main__.py").write_text("# Unrelated entrypoint.\n")
    elif broken_boundary == "module-entrypoint":
        entrypoint = import_root / "sample_project/__main__.py"
        entrypoint.write_text(entrypoint.read_text() + '\nif __name__ == "__main__":\n    raise SystemExit("broken entrypoint")\n')
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "tests/test_smoke.py"], cwd=project,
        env={**os.environ, "PYTHONPATH": str(import_root)}, capture_output=True, text=True, timeout=30,
    )
    if broken_boundary:
        assert result.returncode == 1, result.stdout + result.stderr
        assert "failed" in result.stdout, result.stdout + result.stderr
    else:
        assert result.returncode == 0, result.stdout + result.stderr


def test_claude_compatibility_bridge_renders_actual_root_import(template_source, tmp_path):
    project = tmp_path / "consumer"
    render(template_source, project)
    assert (project / "CLAUDE.md").read_text() == "@AGENTS.md\n"
