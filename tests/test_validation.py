"""Trust-boundary validation must fail before producing target files."""

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
