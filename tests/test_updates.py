"""Actual Git-backed managed updates/adoption preserve consumer authority and product/settings bytes."""

import json
import shutil

from copier import run_copy, run_update
from copier.errors import UserMessageError
import pytest

from helpers import MARKET, PROFILE_PLUGINS, assert_selection, configs, git, snapshot


@pytest.fixture
def versioned_source(template_source, tmp_path):
    source = tmp_path / "versioned-source"
    shutil.copytree(template_source, source, symlinks=True)
    git(source, "init", "--template=", "-b", "main")
    git(source, "add", ".")
    git(source, "commit", "-m", "Disposable template fixture")
    git(source, "tag", "v1.0.0")
    return source


def test_guidance_adoption_preserves_preowned_host_settings_and_root_authority(template_source, tmp_path):
    project = tmp_path / "consumer"
    (project / ".codex").mkdir(parents=True)
    (project / ".claude").mkdir()
    custom = {".codex/config.toml": 'model = "existing-model"\n',
              ".claude/settings.json": '{"permissions":{"deny":["Bash(rm *)"]}}\n',
              "AGENTS.md": "Existing project safety authority.\n"}
    for name, body in custom.items():
        (project / name).write_text(body)
    run_copy(str(template_source), project, data={"project_name": "consumer", "adoption": "guidance"},
             defaults=True, quiet=True, overwrite=True, unsafe=False, skip_tasks=True)
    for name, body in custom.items():
        assert (project / name).read_text() == body
    assert not (project / "src").exists() and not (project / "package.json").exists()


def test_git_managed_ref_and_profile_update_preserves_settings_policy_and_product(versioned_source, tmp_path):
    source = versioned_source
    project = tmp_path / "consumer"
    run_copy(str(source), project, vcs_ref="v1.0.0", data={"project_name": "consumer", "profile": "nextjs",
                                                      "agent_skills_repository": "My-Org/agent-skills"},
             defaults=True, quiet=True, unsafe=False, skip_tasks=True)
    codex_path = project / ".codex/config.toml"
    codex_path.write_text('model = "consumer-model"\n\n' + codex_path.read_text())
    claude_path = project / ".claude/settings.json"
    claude = json.loads(claude_path.read_text())
    claude["permissions"] = {"deny": ["Bash(rm *)"]}
    claude_path.write_text(json.dumps(claude, indent=2) + "\n")
    policy = project / "AGENTS.md"
    policy.write_text(policy.read_text() + "\nConsumer safety policy.\n")
    product = project / "src/app/page.tsx"
    product.write_text(product.read_text() + "\n// Consumer product behavior\n")
    before = {name: (project / name).read_bytes() for name in ("AGENTS.md", "src/app/page.tsx", "package.json", "README.md")}
    git(project, "init", "--template=", "-b", "main")
    git(project, "add", ".")
    git(project, "commit", "-m", "Disposable customized consumer")
    guidance = source / "template/.agents/README.md.jinja"
    guidance.write_text(guidance.read_text() + "\nReviewed template update.\n")
    git(source, "add", ".")
    git(source, "commit", "-m", "Disposable guidance revision")
    git(source, "tag", "v2.0.0")
    run_update(project, vcs_ref="v2.0.0", data={"profile": "python-fastapi", "agent_skills_ref": "v0.2.0"},
               defaults=True, quiet=True, overwrite=True, unsafe=True, skip_tasks=True)
    assert_selection(project, PROFILE_PLUGINS["python-fastapi"])
    codex, claude = configs(project)
    assert codex["model"] == "consumer-model"
    assert codex["marketplaces"][MARKET]["ref"] == "v0.2.0"
    assert claude["permissions"] == {"deny": ["Bash(rm *)"]}
    assert {name: (project / name).read_bytes() for name in before} == before
    assert not (project / "pyproject.toml").exists()
    assert "Reviewed template update." in (project / ".agents/README.md").read_text()
    assert not list(project.rglob("*.rej"))


@pytest.mark.parametrize("old_delivery", ["local", "plugins"])
def test_real_draft_source_upgrade_rejects_before_retiring_customized_resources(
    template_source, tmp_path, old_delivery,
):
    source = tmp_path / "versioned-source"
    shutil.copytree(template_source, source, symlinks=True)
    config = source / "copier.yml"
    current = config.read_text()
    guard = """    {% if agent_delivery is defined or agent_delivery_baseline is defined or rust_async is defined %}
    Pre-publication local/dual-delivery answers require separate reviewed re-enrollment; do not update them in place.
    {% elif not"""
    assert guard in current
    config.write_text(current.replace(guard, "    {% if not", 1) + """
agent_delivery:
  type: str
  choices: [local, plugins]
  default: local
""")
    legacy = source / "template/.agents/skills/legacy-custom/SKILL.md"
    legacy.parent.mkdir(parents=True)
    legacy.write_text("Legacy draft resource.\n")
    git(source, "init", "--template=", "-b", "main")
    git(source, "add", ".")
    git(source, "commit", "-m", "Disposable genuine guardless draft source")
    git(source, "tag", "v1.0.0")
    project = tmp_path / "consumer"
    run_copy(str(source), project, vcs_ref="v1.0.0", data={
        "project_name": "consumer", "agent_delivery": old_delivery,
    }, defaults=True, quiet=True, unsafe=False, skip_tasks=True)
    customized = project / ".agents/skills/legacy-custom/SKILL.md"
    customized.write_text("Consumer-owned legacy adaptation must survive.\n")
    git(project, "init", "--template=", "-b", "main")
    git(project, "add", ".")
    git(project, "commit", "-m", "Disposable customized draft consumer")
    config.write_text(current)
    shutil.rmtree(source / "template/.agents/skills")
    guidance = source / "template/.agents/README.md.jinja"
    guidance.write_text(guidance.read_text() + "\nNew revision must not reach rejected consumer.\n")
    git(source, "add", ".")
    git(source, "commit", "-m", "Disposable plugin-only revision retiring draft resources")
    git(source, "tag", "v2.0.0")
    before = snapshot(project)
    with pytest.raises((ValueError, UserMessageError), match="re-enrollment"):
        run_update(project, vcs_ref="v2.0.0", defaults=True, quiet=True,
                   overwrite=True, unsafe=True, skip_tasks=True)
    assert snapshot(project) == before
    assert customized.read_text() == "Consumer-owned legacy adaptation must survive.\n"


def test_monorepo_updates_preserve_root_group_product_seeds(versioned_source, tmp_path):
    source = versioned_source
    project = tmp_path / "consumer"
    run_copy(str(source), project, vcs_ref="v1.0.0", data={
        "project_name": "consumer", "layout": "monorepo", "monorepo_preset": "python-next",
    }, defaults=True, quiet=True, unsafe=False, skip_tasks=True)
    product = project / "apps/api/src/api/app.py"
    product.write_text(product.read_text() + "\n# Consumer-owned behavior\n")
    deleted = project / "apps/web/src/app/page.tsx"
    deleted.unlink()
    before = snapshot(project / "apps")
    git(project, "init", "--template=", "-b", "main")
    git(project, "add", ".")
    git(project, "commit", "-m", "Disposable customized monorepo")
    guidance = source / "template/.agents/README.md.jinja"
    guidance.write_text(guidance.read_text() + "\nReviewed routing update.\n")
    native = next((source / "blueprints/python-fastapi/src").rglob("app.py.jinja"))
    native.write_text(native.read_text() + "\n# New seed must not replace existing product\n")
    git(source, "add", ".")
    git(source, "commit", "-m", "Disposable new template seed and guidance")
    git(source, "tag", "v2.0.0")
    run_update(project, defaults=True, quiet=True, overwrite=True, unsafe=True, skip_tasks=True)
    assert snapshot(project / "apps") == before
    assert not deleted.exists() and not (project / "src").exists()
    assert "Reviewed routing update." in (project / ".agents/README.md").read_text()
    assert not list(project.rglob("*.rej"))


def test_retiring_shared_form_copies_preserves_all_existing_consumer_bytes(template_source, tmp_path):
    source = tmp_path / "versioned-source"
    shutil.copytree(template_source, source, symlinks=True)
    config = source / "copier.yml"
    current = config.read_text()
    config.write_text(current.replace("  - /.agents/templates\n", ""))
    forms = source / "template/.agents/templates"
    forms.mkdir(parents=True, exist_ok=True)
    for name in ("adr", "change-spec", "folder-readme", "package-readme", "task-brief"):
        (forms / f"{name}.md").write_text(f"Old reusable {name} form.\n")
    git(source, "init", "--template=", "-b", "main")
    git(source, "add", ".")
    git(source, "commit", "-m", "Disposable old template with copied forms")
    git(source, "tag", "v1.0.0")
    project = tmp_path / "consumer"
    run_copy(str(source), project, vcs_ref="v1.0.0", data={"project_name": "consumer"},
             defaults=True, quiet=True, unsafe=False, skip_tasks=True)
    legacy = project / ".agents/templates"
    (legacy / "change-spec.md").write_text("Consumer customized contract format must survive.\n")
    (legacy / "local-only.md").write_text("User-owned resource, never template-owned.\n")
    before = snapshot(legacy)
    git(project, "init", "--template=", "-b", "main")
    git(project, "add", ".")
    git(project, "commit", "-m", "Disposable consumer with customized and local resources")
    config.write_text(current)
    shutil.rmtree(forms)
    routing = source / "template/.agents/README.md.jinja"
    routing.write_text(routing.read_text() + "\nReviewed central resource routing.\n")
    git(source, "add", ".")
    git(source, "commit", "-m", "Disposable template with plugin-owned forms")
    git(source, "tag", "v2.0.0")
    run_update(project, vcs_ref="v2.0.0", defaults=True, quiet=True,
               overwrite=True, unsafe=True, skip_tasks=True)
    assert snapshot(legacy) == before, "Retiring generic copies must not unlink consumer-owned forms"
    assert "Reviewed central resource routing." in (project / ".agents/README.md").read_text()
    assert not list(project.rglob("*.rej"))
