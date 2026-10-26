# Focused scaffold verification

Run `uv run --locked pytest` from the source root. Copier and the existing lock own the environment.

- `test_plugin_only.py`: actual eight-profile host matrices, host-known local/private sources, no payload/role or shared-manual copies, native presets including Python API
  + Next, repeated-profile custom composition, package routing, capability/hook opt-in and guarded Python/Rust smoke.
- `test_validation.py`: unsafe names/source/refs, unknown profiles, component collisions and internal-input protection.
- `test_updates.py`: disposable Git-backed managed ref/profile updates, root apps/packages seed/root-policy/custom-settings preservation,
  adoption safeguards and explicit rejection of recorded unpublished dual-mode answers.
- `test_installation.py`: trusted native task selection/deduplication, render-only/trust gates, fail-stop and explicit-source
  rejection, plus adoption/update non-execution. A recording CLI runs only in isolated Plumbum HOME/CODEX_HOME/PATH.
- `test_plugin_contract.py`: synthetic positive/negative central-catalog identity and dependency-closure fixtures.

`conftest.py` lazily renders each standalone profile once into a read-only session cache; mutation tests use fresh
copies. Tests do not depend on an unversioned neighboring checkout, install product dependencies or execute plugins.
Git commits/tags exist only inside disposable fixtures. Rust smoke is offline and explicitly skipped when Cargo is
unavailable. Native scaffold checks do not prove full product behavior, security, interoperability or hardware safety.

When both reviewed sources are explicitly checked out, additionally run:

```bash
uv run --locked python scripts/check_plugin_contract.py ../agent-skills
```

This local integration check reads the catalog without fetching, copying inventory/payloads, building, installing or
trusting plugins. Host/App discovery, plugin loading, project/hook trust, publishing and physical checks remain separate.
