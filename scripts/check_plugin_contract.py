"""Check native scaffold selections against an explicitly supplied local central catalog."""

import argparse
from itertools import product
import json
from pathlib import Path


def check_contract(registry, catalog):
    if catalog.get("schema_version") != 1 or catalog.get("marketplace") != registry["marketplace"]:
        raise ValueError("Central catalog schema/marketplace does not match the scaffold contract")
    plugins = catalog["plugins"]
    by_id = {entry["id"]: entry for entry in plugins}
    if len(by_id) != len(plugins):
        raise ValueError("Central catalog contains duplicate plugin IDs")
    referenced = set(registry["common_plugins"]) | {registry["hook_plugin"]}
    for entry in [*registry["profiles"], *registry["capabilities"]]:
        referenced.update(entry["plugins"])
    if referenced != set(by_id):
        raise ValueError(f"Plugin identity mismatch: scaffold-only={sorted(referenced - by_id.keys())}; "
                         f"central-only={sorted(by_id.keys() - referenced)}")
    for profile in registry["profiles"]:
        for capabilities in product((False, True), repeat=len(registry["capabilities"]) + 1):
            selected = set(registry["common_plugins"]) | set(profile["plugins"])
            for enabled, capability in zip(capabilities, registry["capabilities"]):
                if enabled:
                    selected.update(capability["plugins"])
            if capabilities[-1]:
                selected.add(registry["hook_plugin"])
            for name in selected:
                missing = set(by_id[name].get("requires", [])) - selected
                if missing:
                    raise ValueError(f"Profile {profile['id']}: {name} is missing required plugins {sorted(missing)}")
    return sorted(referenced)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Reviewed local agent-skills checkout containing catalog.json")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    try:
        registry = json.loads((root / "blueprints/profiles.json").read_text())
        catalog = json.loads((args.source / "catalog.json").read_text())
        names = check_contract(registry, catalog)
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, f"Plugin contract failed: {error}\n")
    print("Plugin identity and selection dependency closure verified: " + ", ".join(names))


if __name__ == "__main__":
    main()
