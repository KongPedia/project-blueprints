# Native profile fragments

These are the actual native source, manifest and README fragments assembled by Copier, not folders to copy manually.
`template/` combines selected fragments with shared guidance. Generated repositories do not contain `blueprints/` or
`template/` themselves.

| Selection | Profile ID | Monorepo placement |
| --- | --- | --- |
| General Python | `python` | Independent app/service in `apps/<name>` or shared code in `packages/<name>` |
| FastAPI backend | `python-fastapi` | `apps/<name>` |
| Litestar backend | `python-litestar` | `apps/<name>` |
| React frontend · Vite | `react-typescript` | `apps/<name>` |
| NestJS backend | `nestjs` | `apps/<name>` |
| Next.js full-stack | `nextjs` | `apps/<name>` |
| Rust | `rust` | Independent app/service in `apps/<name>` or shared code in `packages/<name>` |
| C++ firmware | `cpp-firmware` | `apps/<name>` |

Single projects assemble one native profile at the root. Native Copier presets compose packages under `apps` or
`packages`; `python-backend` selects API + worker + shared Python, and `python-next` selects API + Next.js without YAML. Advanced custom answers support arbitrary
names and repeated profiles. No wrapper wizard is required or maintained.

[profiles.json](profiles.json) owns native metadata and plugin identities—not reusable skill names or a central catalog
copy. Selection unions `common`, each actual package's language/framework/API/UI plugins and explicit optional robotics
or session-guidance. Rust includes task-conditional async guidance; no separate async bundle or Tokio selection exists.
All optional capabilities/hooks default off. A trusted new-project copy installs selected Codex plugins from the registered host index; `--skip-tasks` renders only.
Generation installs no product dependencies or SDKs, starts no services and contacts no hardware.

Native fragments are code seeds, not product behavior or interoperability evidence. See the [root README](../README.md)
and [adoption procedure](../docs/adoption.md) for safe new-project generation, re-enrollment and managed updates.
