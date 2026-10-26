# Explicit local contract check

Native Copier is the only scaffold UI. Reusable procedures, resources, generic references and roles are not mirrored
or synchronized here. With an explicitly reviewed central source checkout available, run:

```bash
uv run --locked python scripts/check_plugin_contract.py ../agent-skills
```

The standard-library check compares referenced public plugin IDs and dependency closure against that checkout's
`catalog.json`. It does not fetch, copy inventory/payloads, install, build, trust or execute plugins. Ordinary unit tests
use synthetic fixtures and do not depend on an unversioned neighboring checkout.
