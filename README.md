# Project Blueprints

A native **Copier template** for Python, React, NestJS, Next.js, Rust, C++ firmware and mixed-language repositories.
It creates native code layouts and project-owned guidance, then installs the selected `agent-skills` plugins through
Codex without copying skill bodies. A marketplace is a plugin index: it can be **local or private**, not a public store.

## Create a project

Run native Copier from the directory where you want the new project:

```bash
uvx copier copy --trust \
  git@github.com:KongPedia/project-blueprints.git ./my-project
```

Git access to the private template is required; no manual clone or change into the template directory is needed.
Copier asks the project name, single/monorepo, profile/composition and optional capability questions. Without
`--vcs-ref`, native Copier selects the latest suitable stable template tag. Add `--vcs-ref v0.1.0` to freeze this release.

The existing local-source command still works:

```bash
uvx copier copy --trust \
  /path/to/project-blueprints ./my-project
```

**Use a new destination.** Native Copier permits existing-directory merges; it does not enforce an existing-path
abort or ask a separate installation-confirmation question. `--trust` authorizes reviewed template code execution;
it is not Codex workspace/hook trust. Replace it with `--skip-tasks` for files only, without plugin installation.

Its copy-only task runs `codex plugin add` for the selected union, without per-plugin input or skill copies.
Keep the default empty `agent_skills_repository`. Register the reviewed skills index **once per host** first:

```bash
codex plugin marketplace add /path/to/agent-skills
```

If the first copy reports `plugin ... was not found in marketplace konglabs-agent-skills`, register the source and
verify any existing same-name source/cache. The Python task already prints this recovery hint; it never retargets a
source automatically. Then follow generated `.agents/plugin-setup.md` or retry into a new path after inspecting failure
output. The host path is not committed product configuration. For a private Git source or Claude, see
[Agent Skills host setup](https://github.com/KongPedia/agent-skills/blob/v0.1.0/docs/hosts.md) and
[installation boundaries](docs/adoption.md#automatic-codex-installation).

| Technology | Profile | Starting point |
| --- | --- | --- |
| Python | General Python | Importable src-layout package and execution entrypoint |
| Python | FastAPI / Litestar backend | HTTP app, health route and boundary tests |
| TypeScript | React frontend · Vite | Browser-only React shell |
| TypeScript | NestJS backend | Nest module/controller and HTTP test |
| TypeScript | Next.js full-stack | App Router page and Route Handler |
| Rust | Rust | One Cargo package with `lib.rs` and `main.rs` |
| C++ | Firmware | PlatformIO host-only starter; no board/pins |

Monorepos compose whole packages under root `apps/<name>` or `packages/<name>`. Seven built-in compositions include
Python API + worker + shared Python, Python API + React, Python API + Next, Nest + React, robotics + web, headless and firmware. Python API compositions
choose FastAPI/Litestar. Custom component names use advanced YAML answers, not another generator or preset directory.
Robotics installs no SDK. The advisory hook defaults off and needs separate trust; Rust async guidance adds no runtime.

## Source is not the generated product

| Location | Role |
| --- | --- |
| `copier.yml` | Native questions, selection, copy-only Codex installation task and update boundaries |
| `blueprints/` | Eight native fragments and profile-to-plugin ID mapping |
| `template/` | Product guidance, local contract locations, design brief and output assembly |
| `docs/` | Template-maintainer documentation only; not copied into products |
| `scripts/`, `tests/` | Template contract checks and regression tests |

There is no dummy root product source/bin tree, root product design brief, skill mirror, custom CLI or second agent catalog.
Internal relative symlinks mount native fragments once; Copier emits ordinary files. Preserve symlinks in source Git
checkouts. A single package uses its root manifest and native `src/`; a monorepo retains each package's native `src/`
inside root `apps/` or `packages/`, without an empty outer `src/`. Packages initially own independent environments,
manifests, locks and checks. Adopt uv/npm/Cargo workspaces only for actual dependency and environment ownership;
mixed languages do not imply one lock, runtime, deployment or working FFI/IPC.

Generated `.agents/README.md` owns task/package routing; `.agents/plugin-setup.md` owns selected host setup commands.
[Product docs](template/docs/) retain actual local structure, contracts and decisions. Root product `scripts/` and `bin/`
are maintenance locations, not alternate product-module owners; tests follow native packages, with root integration
checks when needed. A README keeps an otherwise-empty location in Git; `.gitkeep` is only needed without another file.

Reusable blank forms, TDD/SDD/selective DDD, source-first investigation and worked architecture/robotics references
live with shared skills. Common provides task briefs through `writing-plans`, change specs through
`spec-driven-development`, README guidance through `docs-sync`, and the existing `domain-modeling/ADR-FORMAT.md`.
Copier does not copy those assets into `.agents/templates`. Product-specific filled specs, ADRs and design decisions
remain local; [DESIGN.md](template/DESIGN.md) is a product brief, not a shared methodology manual.

## Remote templates and updates

Copier fetches the template Git source directly; it does not need an installed template package. `--vcs-ref` pins a
reviewed template revision. With no template ref, Copier selects the latest suitable stable tag, not development HEAD.
Retain reviewed source history for durable updates. This template and the skills provider have coordinated `v0.1.0`
private releases; a GitHub template-repository flag is not needed to use Copier.

The skills source is registered separately with the host. Advanced project-owned Git source/ref settings use raw
render-only Copier (`--skip-tasks`) and manual source/cache review: automatic installation rejects a nonempty repository
before any add. Source/ref settings alone do not prove which cached Git payload Codex will use.
See [adoption](docs/adoption.md) and [updates](docs/updates.md).

Copier updates project guidance/configuration, not product seeds or installed plugins. The installation task runs only
for a new project copy; guidance adoption and updates do not install. Shared plugin releases refresh through the host.
Preserve clean history, unrelated settings and local policy; review old draft re-enrollment rather than forcing updates.

```bash
uv run --locked pytest
```

- [Maintainer docs](docs/README.md), [source references](docs/sources.md)
- [Observed verification](docs/verification.md), [evaluation limits](docs/evaluation.md), [license boundary](THIRD-PARTY-NOTICES.md)

CI configuration and local checks are not actual GitHub execution. Optional cross-repository CI uses reviewed
`AGENT_SKILLS_CONTRACT_REF` / `BLUEPRINTS_CONTRACT_REF` after remote access exists; an unset ref skips, not passes, that job.
Trusted new-project generation installs selected Codex plugins in host state. It does not install product dependencies
or Claude plugins, approve workspace/hooks, run apps/CI, initialize/push Git, deploy or touch hardware. Failure stops the
install chain without rolling back already installed plugins; `--skip-tasks` leaves rendering only.
