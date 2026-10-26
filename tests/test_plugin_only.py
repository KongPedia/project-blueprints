"""Plugin-only scaffolding boundaries, independent of the unpublished central checkout."""

from configparser import ConfigParser
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tomllib

from copier import run_copy
import pytest

from helpers import PROFILE_PLUGINS, assert_local_links, assert_selection, configs, render


def test_new_project_does_not_copy_any_reusable_skill_body(template_source, tmp_path):
    project = tmp_path / "consumer"
    run_copy(str(template_source), project, data={"project_name": "consumer"},
             defaults=True, quiet=True, unsafe=False, skip_tasks=True)
    assert not (project / ".agents/skills").exists(), "Native Copier must select plugins, not copy skill Markdown"
    assert not (project / ".agents/licenses").exists()
    assert not (Path(__file__).resolve().parents[1] / ".agents/skills").exists(), "Only the central source owns reusable skills"


def test_default_selection_uses_host_source_without_publishing_or_copying_maintainer_docs(rendered_profile):
    project = rendered_profile("python")
    codex, claude = configs(project)
    assert "marketplaces" not in codex, "Default projects must use the host-known local/private source"
    assert "extraKnownMarketplaces" not in claude
    for name in ("docs/adoption.md", "docs/agent-distribution.md", "docs/sources.md", "docs/updates.md",
                 "docs/skill-inventory.md", ".agents/plugin-selection.json", ".agents/package-routing.md",
                 "blueprints", "template", "presets"):
        assert not (project / name).exists(), f"Maintainer/redundant source leaked into product: {name}"
    setup = (project / ".agents/plugin-setup.md").read_text()
    assert "codex plugin add common@konglabs-agent-skills" in setup
    assert "codex plugin add python@konglabs-agent-skills" in setup
    assert "KongPedia/agent-skills" not in setup


@pytest.mark.parametrize("profile", PROFILE_PLUGINS)
def test_native_profiles_select_complete_host_matrix_without_payload_copies(rendered_profile, profile):
    project = rendered_profile(profile)
    assert_selection(project, PROFILE_PLUGINS[profile])
    codex, claude = configs(project)
    assert "marketplaces" not in codex and "extraKnownMarketplaces" not in claude
    if profile.startswith("python"):
        assert tomllib.loads((project / "pyproject.toml").read_text())["project"]["name"] == "sample-project"
    elif profile == "rust":
        assert tomllib.loads((project / "Cargo.toml").read_text())["package"]["name"] == "sample-project"
    elif profile == "cpp-firmware":
        ini = ConfigParser()
        ini.read(project / "platformio.ini")
        assert ini["platformio"]["default_envs"] == "native"
        assert set(ini.sections()) == {"platformio", "env:native"}
    else:
        assert json.loads((project / "package.json").read_text())["name"] == "sample-project"
    assert any((project / "src").rglob("*"))
    assert all(not path.is_symlink() and "{{" not in path.name and "{%" not in path.name
               for path in project.rglob("*"))
    assert_local_links(project)


@pytest.mark.parametrize(("preset", "expected_profiles", "expected_plugins"), [
    ("python-backend", {"python-fastapi", "python"}, PROFILE_PLUGINS["python-fastapi"]),
    ("python-next", {"python-fastapi", "nextjs"}, PROFILE_PLUGINS["python-fastapi"] | PROFILE_PLUGINS["nextjs"]),
    ("python-web", {"python-litestar", "react-typescript"}, PROFILE_PLUGINS["python-litestar"] | PROFILE_PLUGINS["react-typescript"]),
    ("headless", {"python-fastapi", "python", "rust"}, PROFILE_PLUGINS["python-fastapi"] | PROFILE_PLUGINS["rust"]),
])
def test_native_monorepo_presets_derive_plugin_union_without_yaml(
    template_source, tmp_path, preset, expected_profiles, expected_plugins,
):
    project = tmp_path / "consumer"
    render(template_source, project, layout="monorepo", monorepo_preset=preset,
           api_framework="python-litestar" if preset == "python-web" else "python-fastapi")
    assert_selection(project, expected_plugins)
    from copier._template import load_template_config

    answers = load_template_config(project / ".copier-answers.yml")
    assert {entry["profile"] for entry in answers["components"]} == expected_profiles
    for entry in answers["components"]:
        assert (project / entry["kind"] / entry["name"] / "README.md").is_file()
    assert_local_links(project)


def test_custom_components_allow_repeated_profiles_but_keep_package_routing_separate(template_source, tmp_path):
    project = tmp_path / "consumer"
    render(template_source, project, layout="monorepo", components=[
        {"name": "events-api", "kind": "apps", "profile": "python-fastapi"},
        {"name": "worker", "kind": "apps", "profile": "python"},
        {"name": "console", "kind": "apps", "profile": "nextjs"},
    ])
    assert_selection(project, PROFILE_PLUGINS["python-fastapi"] | PROFILE_PLUGINS["nextjs"])
    routing = (project / ".agents/README.md").read_text()
    api, web = routing.split("### `apps/events-api`")[1].split("### `apps/console`")
    assert "fastapi@" in api and "nextjs@" not in api
    assert "nextjs@" in web and "python@" not in web
    assert_local_links(project)


@pytest.mark.parametrize(("robotics", "hooks"), [(False, False), (True, False), (False, True), (True, True)])
def test_optional_plugins_need_explicit_selection_not_trust(template_source, tmp_path, robotics, hooks):
    project = tmp_path / "consumer"
    render(template_source, project, profile="rust", robotics=robotics, enable_agent_hooks=hooks)
    expected = PROFILE_PLUGINS["rust"] | ({"robotics"} if robotics else set()) | ({"session-guidance"} if hooks else set())
    assert_selection(project, expected)
    assert not (project / "docs/robotics.md").exists()
    assert ("## Device-I/O tasks" in (project / ".agents/README.md").read_text()) is robotics
    setup = (project / ".agents/plugin-setup.md").read_text()
    assert "asynchronous" in setup and "/hooks" in setup and "do not load" in setup
    assert "tokio" not in (project / "src/main.rs").read_text().lower()


def test_python_seed_import_and_execution_have_no_output_or_import_side_effects(rendered_profile):
    project = rendered_profile("python")
    for args in (["-c", "import sample_project; import sample_project.__main__"], ["-m", "sample_project"]):
        result = subprocess.run([sys.executable, "-E", "-B", *args], cwd=project / "src",
                                capture_output=True, text=True, timeout=15)
        assert (result.returncode, result.stdout, result.stderr) == (0, "", "")


def test_rust_seed_keeps_native_library_and_binary_buildable_offline(rendered_profile, tmp_path):
    cargo = shutil.which("cargo")
    if not cargo:
        pytest.skip("Cargo unavailable: native Rust compile smoke not checked")
    project = tmp_path / "consumer"
    shutil.copytree(rendered_profile("rust"), project)
    manifest = tomllib.loads((project / "Cargo.toml").read_text())
    name = manifest["package"]["name"]
    result = subprocess.run([cargo, "build", "--offline", "--lib", "--bin", name], cwd=project,
                            capture_output=True, text=True, timeout=90)
    assert result.returncode == 0, result.stdout + result.stderr
    result = subprocess.run([cargo, "run", "--offline", "--quiet", "--bin", name], cwd=project,
                            capture_output=True, text=True, timeout=90)
    assert (result.returncode, result.stdout, result.stderr) == (0, "", "")


def test_monorepo_uses_root_package_groups_without_an_empty_outer_src(template_source, tmp_path):
    project = tmp_path / "consumer"
    render(template_source, project, layout="monorepo", monorepo_preset="python-web")
    assert (project / "apps/api/src/api/app.py").is_file()
    assert (project / "apps/web/src/app/App.tsx").is_file()
    assert not (project / "src").exists()
    assert not (project / "packages").exists(), "Do not create unused package groups"
    for manual in ("development.md", "architecture.md", "robotics.md"):
        assert not (project / "docs" / manual).exists(), "Shared methodology belongs in plugins"
    assert_local_links(project)


def test_generic_artifact_forms_are_plugin_resources_not_consumer_copies(rendered_profile):
    project = rendered_profile("python")
    assert not (project / ".agents/templates").exists(), "Common assets belong in the installed plugin"
    assert not (project / "src/README.md").exists(), "Native packages already own their source layout"
    assert_local_links(project)
