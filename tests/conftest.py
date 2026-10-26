"""One read-only source snapshot and lazy read-only native-profile renders per test session."""

from pathlib import Path
import shutil

from copier import run_copy
import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="session")
def template_source(tmp_path_factory):
    source = tmp_path_factory.mktemp("source") / "project-blueprints"
    shutil.copytree(ROOT, source, symlinks=True, ignore=shutil.ignore_patterns(
        ".git", ".venv", ".pytest_cache", "__pycache__", ".DS_Store", ".omx", "node_modules", "target",
    ))
    return source.resolve()


@pytest.fixture(scope="session")
def rendered_profile(template_source, tmp_path_factory):
    cache = {}

    def get(profile):
        if profile not in cache:
            project = tmp_path_factory.mktemp(profile) / "sample-project"
            run_copy(str(template_source), project, data={"project_name": "sample-project", "profile": profile},
                     defaults=True, quiet=True, unsafe=False, skip_tasks=True)
            cache[profile] = project
        return cache[profile]

    return get
