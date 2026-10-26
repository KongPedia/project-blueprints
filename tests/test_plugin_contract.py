"""Offline contract-checker fixtures; ordinary tests never read a neighboring checkout."""

from copy import deepcopy
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("check_plugin_contract", ROOT / "scripts/check_plugin_contract.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


@pytest.fixture
def contract():
    registry = json.loads((ROOT / "blueprints/profiles.json").read_text())
    names = set(registry["common_plugins"]) | {registry["hook_plugin"]}
    for entry in registry["profiles"] + registry["capabilities"]:
        names.update(entry["plugins"])
    catalog = {"schema_version": 1, "marketplace": registry["marketplace"],
               "plugins": [{"id": name, "requires": []} for name in sorted(names)]}
    for plugin in catalog["plugins"]:
        if plugin["id"] == "nextjs":
            plugin["requires"] = ["typescript", "react-ui", "api-contracts"]
    return registry, catalog


def test_matching_plugin_identity_and_selection_dependency_contract(contract):
    registry, catalog = contract
    assert set(module.check_contract(registry, catalog)) == {entry["id"] for entry in catalog["plugins"]}


@pytest.mark.parametrize("failure", ["unknown", "missing-dependency", "duplicate", "marketplace"])
def test_contract_checker_rejects_broken_identity_or_dependency_contract(contract, failure):
    registry, catalog = deepcopy(contract)
    if failure == "unknown":
        registry["profiles"][0]["plugins"].append("unknown")
    elif failure == "missing-dependency":
        next(entry for entry in catalog["plugins"] if entry["id"] == "python")["requires"] = ["rust"]
    elif failure == "duplicate":
        catalog["plugins"].append(catalog["plugins"][0])
    else:
        catalog["marketplace"] = "different-marketplace"
    with pytest.raises(ValueError):
        module.check_contract(registry, catalog)
