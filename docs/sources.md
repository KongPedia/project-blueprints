# Sources and applicability

Official documentation and upstream sources inform decisions; they do not prove this starter installed or ran a tool.
This is an adaptation combining native source/manifests and shared guidance, not a universal directory standard.
The canonical imported-file inventory, immutable upstream revisions, adaptations, hashes and retained licenses belong
to the separate `agent-skills` repository and each packaged payload. This template records profile-to-plugin selection,
not another skill implementation catalog. This maintainer reference is not a generated inventory or copied product document.

## Python

- [PyPA: src layout vs flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/):
  import/distribution boundaries; a directory named `src` does not implement packaging or installation.
- [uv workspaces](https://docs.astral.sh/uv/concepts/projects/workspaces/): member, environment and lock sharing when
  adopting a real workspace, not a requirement to combine independent services into one environment.
- [Cosmic Python project structure](https://www.cosmicpython.com/book/appendix_project_structure): responsibility and
  dependency-direction alternatives for complex backends, not mandatory layers/interfaces for a small API.
- [Python asyncio tasks](https://docs.python.org/3/library/asyncio-task.html) and
  [typing](https://docs.python.org/3/library/typing.html): cancellation, thread-offload limits and annotation semantics.
  Thread offload does not guarantee CPU parallelism; annotations do not validate runtime input.

Configuration/types, resource cleanup and async criteria already have homes in engineering/Python guidance; avoid
adding overlapping skills merely to increase the catalog.

## Optional robotics software

- [ROS 2 managed node lifecycle](https://design.ros2.org/articles/node_lifecycle.html): startup/state/shutdown concepts,
  not a requirement to install ROS or adopt its lifecycle in every robotics system.
- Installed common/robotics procedures own the architecture and robotics worked references; product docs retain only
  actual local contracts. No transport/SDK is implied by those design examples.

Robotics is an opt-in capability for any selected language. It is neither a Python framework nor automatic hardware
access. Selected projects enable the robotics bundle containing `robotics-software` and its shared worked reference;
file/test presence is not physical-safety proof.

## Framework-specific guidance

- [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/) and
  [lifespan testing](https://fastapi.tiangolo.com/advanced/testing-events/): HTTP contracts and resource-lifetime tests.
  `fastapi-backend` is original task guidance informed by these documents, not a copied upstream skill.
  FastAPI also publishes [official AI agent skills](https://fastapi.tiangolo.com/tutorial/#ai-agent-skills);
  the [pinned 0.162.0 skill and references](https://github.com/fastapi/fastapi/tree/7a0a3f0b286c6c865cf4398ea0e957a87b8bffa4/fastapi/.agents/skills/fastapi)
  are available for deeper framework work. The shared `fastapi` bundle keeps a narrow procedure without imposing a
  wider ORM, CLI or concurrency stack.
- [Litestar 2 dependency injection](https://docs.litestar.dev/2/usage/dependency-injection.html),
  [applications/lifespan](https://docs.litestar.dev/2/usage/applications.html) and
  [testing](https://docs.litestar.dev/2/usage/testing.html): dependency scope versus resource lifetime, isolation and
  real HTTP/lifecycle checks. `litestar-backend` is original scoped guidance for the installed 2.x release, not a copy of
  the broader [first-party skill collection](https://github.com/litestar-org/litestar-skills/tree/150bdbebadf79022bd0440e6f3ddcfde22b74f4e).
  Ecosystem stacks, plugin hooks and ORM/layout preferences are not template requirements.
- [Nest testing](https://docs.nestjs.com/fundamentals/testing) and [migration guide](https://docs.nestjs.com/migration-guide):
  installed-major DI/module/testing and ESM constraints. `nestjs-backend` does not mandate an ORM, database or CQRS.
- [Next AI agents](https://nextjs.org/docs/app/guides/ai-agents): installed-version bundled documentation and managed
  AGENTS blocks. `nextjs-app-router` prioritizes that local documentation; retired `vercel-labs/next-skills` is not vendored,
  and runtime tools, feedback or upgrade workflows are not enabled automatically.

Framework skills are conditional. Do not apply Next server APIs to a React SPA or FastAPI to general Python.
A documentation link does not replace license records or product verification.

## TypeScript and React

- [Compiler options](https://www.typescriptlang.org/docs/handbook/modules/guides/choosing-compiler-options.html): match
  browser/Node/library settings to the execution tool, rather than claiming a universal `tsconfig`.
- [Project references](https://www.typescriptlang.org/docs/handbook/project-references.html): an option for an actual build
  graph, not a requirement to split or connect every package.
- [TypeScript paths](https://www.typescriptlang.org/tsconfig/paths.html): aliases do not rewrite emitted imports or define
  runtime resolution/public exports.
- [React state structure](https://react.dev/learn/choosing-the-state-structure): state ownership, duplication and derived
  values; no state library or newer React API is required.
- [Pinned Bulletproof React structure](https://github.com/alan2207/bulletproof-react/blob/9506629ed003a561c6627735480cce4994244bb4/docs/project-structure.md):
  a feature-oriented reference. This starter adapts `app/features/shared`, not its full dependencies/application code.

## Rust

- [Cargo package layout](https://doc.rust-lang.org/cargo/guide/project-layout.html): native library, executable and test
  conventions, not evidence of product behavior.
- [Cargo workspaces](https://doc.rust-lang.org/cargo/reference/workspaces.html): member/shared-setting design, not automatic
  Python/TypeScript interoperability or a single deployment unit.
Rust skill provenance belongs to the installed shared payload, not the project selection record. SDK, transport,
PyO3, Tokio and hardware contracts are not universal Rust rules. Reach native references through
the generated `.agents/README.md` routing entrypoint.

## Firmware

- [PlatformIO native](https://docs.platformio.org/en/latest/platforms/native.html): a host-only firmware starting point,
  not a physical target or hardware validation.

## Specification workflows

- [Spec Kit existing projects](https://github.com/github/spec-kit/blob/main/docs/guides/existing-projects.md): applying
  specifications while preserving an existing project's rules and current state.
- [OpenSpec concepts](https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md): maintained specifications versus
  change intent.

TDD/SDD/selective DDD and source-first investigation belong to the shared procedures and their references. Root
maintainer docs and generated products do not copy another methodology manual; product specs record actual contracts.

## Curation and distribution

Preserve selected skills' names and provenance while removing or conditioning source-project-specific runtime/safety
assumptions. Shared constraints and adaptations belong to canonical plugin resources. The generated `.agents/README.md` routes
product tasks; root maintainer docs do not duplicate that catalog.
Sources/hashes do not prove execution, fresh-session discovery, model adherence or external compatibility.

- [Git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules): parents refer to another repository's commit.
- [Dependabot ecosystems](https://docs.github.com/en/code-security/reference/supply-chain-security/supported-ecosystems-and-repositories):
  `gitsubmodule` version-update support, not configured skill distribution or fleet automation here.
- [Update strategy](updates.md): shared-plugin refresh versus project-owned Copier configuration; no skill submodule.

## Source and output ownership

`agent-skills` owns canonical procedures and closed plugin payloads. This template owns native scaffolding and actual
product-local contracts under `template/`; reusable blank forms belong to Common skill assets; root docs are maintainer-only. Shared bodies/catalogs/generic role implementations
are not mirrored. A local/private registered index needs no public directory listing. Public publication, if later
requested, still needs original-license and secret/proprietary-scope review.

## Agent host packaging and selection

- [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins): portable root manifest and fixed
  component locations, with a supported Codex compatibility overlay; optional hooks/MCP are not required for skills.
- [Codex skills](https://developers.openai.com/codex/skills): skill procedures/resources and progressive discovery.
- [Codex configuration](https://developers.openai.com/codex/config-reference): effective plugin enable/disable settings
  and trusted-project overrides; omission does not establish that a globally enabled plugin is off.
- [Claude manifest](https://code.claude.com/docs/en/plugins-reference),
  [loading](https://code.claude.com/docs/en/plugins/loading) and
  [installation/updates](https://code.claude.com/docs/en/discover-plugins): host-specific packaging and lifecycle.
- [Source selection and acceptance](adoption.md#plugin-source-selection): separates actual `template/` output, maintainer docs and the
  host-registered local/private plugin source. These references do not establish publication or host installation.
- [Automatic installation boundary](adoption.md#automatic-codex-installation): reviewed native Copier copy tasks invoke
  selected Codex adds only from the pre-registered default host source. Nonempty advanced project repositories fail
  before any add; source/ref or CLI overrides do not attest cached Git source identity. Task authorization does not
  register a source, approve workspace/hooks, install Claude plugins or prove discovery; `--skip-tasks` is render-only.

## Observed upstream distribution patterns

- [Anthropic marketplace at a pinned revision](https://github.com/anthropics/skills/blob/dbd4588f9e1033efb41dad4bef2f7947c8993d44/.claude-plugin/marketplace.json):
  five bundles in one source repository.
- [Vercel collection at a pinned revision](https://github.com/vercel-labs/agent-skills/blob/063bee94c3f4df8453406c830b0a7df0f2860278/README.md):
  skill-CLI installation/copies, not automatically a native plugin.
- [Matt Pocock guide at a pinned revision](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/README.md):
  plugin versus editable local skill copies; avoid both active deliveries.
- [Addy Osmani catalog at a pinned revision](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/.agents/plugins/marketplace.json):
  one whole 25-skill plugin, an alternative to this template's selective language/framework bundles.
- [Claude organization delivery](https://code.claude.com/docs/en/plugins/org) and
  [marketplace maintenance](https://code.claude.com/docs/en/plugins/host-marketplace): trust/source distinctions,
  update policy and versioned releases. These are not evidence of an operating team rollout here.

## Template engine

- Native Copier owns questions, rendering, tasks and updates. It permits existing-directory merges and checks unsafe
  features before questions. Use a new destination; it has no built-in installation-confirmation prompt.
- [Copier creating](https://copier.readthedocs.io/en/stable/creating/): conditional rendering and yielded components.
- [Copier configuring](https://copier.readthedocs.io/en/stable/configuring/): includes, subdirectories, skip/exclude,
  answers and native tasks. `--trust` authorizes reviewed template task execution; it is distinct from agent-host trust.
- [Copier updating](https://copier.readthedocs.io/en/stable/updating/): Git revision/answer-based updates and conflict review.
- [Copier 9.19.1](https://pypi.org/project/copier/9.19.1/): the exact maintainer development pin/minimum, not a required
  user command pin. Native `uvx copier copy --trust` may select a reviewed template release without an explicit ref.
  In this installed version, update safety checks can require task authorization for old task metadata even when
  `--skip-tasks` prevents execution; the actual copy-only task is not a shared-plugin update mechanism.

Reference review date: 2026-10-26. Rolling documentation and package versions can change. Review compatibility, locks
and actual checks when upgrading exact profile pins.
