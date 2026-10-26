"""Shared test I/O: isolated renders, host matrices, and disposable Git fixtures only."""

import json
import re
import subprocess
import tomllib
from urllib.parse import unquote, urlsplit

from copier import run_copy

MARKET = "konglabs-agent-skills"
PROFILE_PLUGINS = {
    "python": {"common", "python"},
    "python-fastapi": {"common", "python", "api-contracts", "fastapi"},
    "python-litestar": {"common", "python", "api-contracts", "litestar"},
    "react-typescript": {"common", "typescript", "react-ui"},
    "nestjs": {"common", "typescript", "api-contracts", "nestjs"},
    "nextjs": {"common", "typescript", "react-ui", "api-contracts", "nextjs"},
    "rust": {"common", "rust"},
    "cpp-firmware": {"common", "cpp-firmware"},
}
KNOWN = set.union(*PROFILE_PLUGINS.values()) | {"robotics", "session-guidance"}


def render(source, project, **data):
    run_copy(str(source), project, data={"project_name": "sample-project", **data},
             defaults=True, quiet=True, unsafe=False, skip_tasks=True)


def configs(project):
    return (tomllib.loads((project / ".codex/config.toml").read_text()),
            json.loads((project / ".claude/settings.json").read_text()))


def assert_selection(project, expected):
    codex, claude = configs(project)
    flags = {f"{name}@{MARKET}": name in expected for name in KNOWN}
    assert {key: value["enabled"] for key, value in codex["plugins"].items()} == flags
    assert claude["enabledPlugins"] == flags
    if "extraKnownMarketplaces" in claude:
        assert claude["extraKnownMarketplaces"][MARKET]["autoUpdate"] is False
    for forbidden in (".agents/skills", ".agents/licenses", ".agents/references", ".agents/skill-sources.json", ".codex/agents"):
        assert not (project / forbidden).exists(), forbidden
    assert not {"agents", "hooks", "trust"} & codex.keys()
    assert "hooks" not in claude


def assert_local_links(project):
    for markdown in project.rglob("*.md"):
        body = re.sub(r"(?ms)^```.*?^```[^\n]*", "", markdown.read_text())
        body = re.sub(r"`[^`\n]*`", "", body)
        for target in re.findall(r"\[[^\]]+\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", body):
            parsed = urlsplit(target.strip("<>"))
            if parsed.scheme or not parsed.path or parsed.path.startswith("/"):
                continue
            assert (markdown.parent / unquote(parsed.path)).exists(), f"{markdown.relative_to(project)} -> {target}"


def git(directory, *args):
    return subprocess.run(["git", "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", *args],
                          cwd=directory, check=True, capture_output=True, text=True).stdout.strip()


def snapshot(project):
    return {path.relative_to(project): path.read_bytes() for path in project.rglob("*")
            if path.is_file() and ".git" not in path.relative_to(project).parts}
