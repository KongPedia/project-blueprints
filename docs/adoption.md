# Generation, adoption and re-enrollment

## Native Copier generation

Run from the parent directory of the new project; no template checkout or custom CLI is required:

```bash
uvx copier copy --trust \
  git@github.com:KongPedia/project-blueprints.git ./my-project
```

The private Git source needs normal Git access. A local checkout works with the same interface:

```bash
uvx copier copy --trust \
  ~/Desktop/workspace/konglabs/project-blueprints ./my-project
```

Native prompts select the project name, single/monorepo, one of eight profiles or seven standard compositions, API
framework when relevant, and optional robotics/advisory hook. No extra profile inventory, preset directory or YAML is
needed for standard cases. With no `--vcs-ref`, Copier selects the latest suitable stable tag; use `--vcs-ref v0.1.0`
for this exact template release. The maintainer lock pins Copier for regression checks; users need not type that pin.

**Always use a new destination.** Native Copier permits existing-directory merges. It has no strict existing-path
abort or separate installation-confirmation question. Review the source before `--trust`: it authorizes template code
execution, not Codex workspace/hook trust. Use `--skip-tasks` instead for render-only generation. Do not force a copy
onto an existing product to change its layout or recover from an installation failure.

## Automatic Codex installation

On a trusted new-project copy, native Copier runs a sequential `codex plugin add <identity>@konglabs-agent-skills`
chain derived from the selected profiles/capabilities. Codex, an accessible registered marketplace and the default empty
`agent_skills_repository` are prerequisites. From this workspace, register the reviewed local index once per host:

```bash
codex plugin marketplace add ~/Desktop/workspace/konglabs/agent-skills
```

If copying reports `plugin ... was not found in marketplace konglabs-agent-skills`, verify the source and perform that
one-time registration. From inside the provider checkout, `codex plugin marketplace add .` is equivalent. If that
name is already registered, inspect its source/cache before changing it; an old index may not contain a new bundle.
The current Python task preserves the native error and prints registration/render-only guidance. It never registers,
retargets or refreshes the host source automatically. Missing Codex also produces an actionable prerequisite hint.

A nonempty project repository is rejected before any plugin add. No copied skill library, product installer or
per-plugin input is used. Installation changes host-scoped state and globally enables the selected identities; it
is not a per-project version lock. The generated complete true/false matrix applies after Codex trusts the project;
monorepo routing is task guidance, not per-folder isolation. Workspace and hook trust remain explicit host actions.

An install failure stops the chain without rolling back earlier host installs. Copier may clean up a newly created
destination; inspect any retained output before recovery. Never force recopy or delete unrelated host plugins to
simulate rollback. Generated `.agents/plugin-setup.md` keeps selected recovery/Claude commands; use `--skip-tasks`
when generation is needed without Codex. No fallback copies Markdown or silently selects another source.
Guidance adoption and updates never run the installation task; see the native trust caveat in
[updates](updates.md#copier-updates-and-preservation).

## Plugin source selection

The default empty `agent_skills_repository` emits the complete team true/false activation matrix, relying on the
host-registered `konglabs-agent-skills` index. No proposed Git URL or machine-specific plugin-source path is committed.
The source contains stable plugin IDs, not a second skill inventory; selected profiles derive the required union.
Package/task routing narrows usage in a monorepo, not through a technical per-folder sandbox.

For a deliberately project-owned Git source, use `--skip-tasks` with advanced `agent_skills_repository=owner/repository`
and a reviewed `agent_skills_ref` through Copier's `-d` or `--data-file` options. This renders native Codex/Claude source
declarations for manual review, not automatic safe source selection. Automatic installation rejects this configuration
before any add; it never tries CLI overrides or silently falls back to another source.

Native Codex can reuse an existing same-name cached Git marketplace despite changed source/ref settings or explicit
CLI overrides. A configuration value, Git ref or successful add is not proof of the actual fetched source or installed
bytes. Deliberately register/refresh and inspect the host source/cache before manual installation. For automatic
installation, first establish the intended host source and retain the default empty project repository. Copier never
retargets that registration or repairs its cache. `stable` only means an approved moving channel when actually maintained;
an immutable ref expresses a requested freeze, not independent installed-payload verification.

Generated `.agents/plugin-setup.md` keeps the selected recovery/Claude commands. Source registration, activation,
trust, role/hook support and refresh behavior have one shared owner: provider host setup (`agent-skills/docs/hosts.md`).

## Noninteractive native answers

Use `--defaults` with explicit answers for scripts. These commands still require a new destination and reviewed
`--trust` authorization, or `--skip-tasks` for rendering only. For a Next.js standalone:

```bash
uvx copier copy --trust --defaults \
  -d project_name=my-web -d layout=single -d profile=nextjs \
  git@github.com:KongPedia/project-blueprints.git ./my-web
```

For Python API + Next with Litestar:

```bash
uvx copier copy --trust --defaults \
  -d project_name=my-product -d layout=monorepo -d monorepo_preset=python-next \
  -d api_framework=python-litestar git@github.com:KongPedia/project-blueprints.git ./my-product
```

Use `profile=python` for general Python, `profile=python-fastapi`/`python-litestar` for single HTTP projects,
`monorepo_preset=python-backend` for Python API + worker + shared Python, or `python-web` for API + React/Vite.
Python API compositions accept `api_framework=python-fastapi` as the alternate framework. These choices scaffold native
packages; they do not implement their interoperability, shared imports, deployment or business behavior.

## Custom composition — advanced

Create an answers file for arbitrary names/placements:

```yaml
project_name: example-product
layout: monorepo
components:
  - {name: api, kind: apps, profile: python-litestar}
  - {name: web, kind: apps, profile: nextjs}
  - {name: core, kind: packages, profile: rust}
```

Pass it with Copier's `--data-file` option. Standard combinations—including Python API + Next—use native preset questions
instead. This is a composition contract, not implemented business behavior or a second answer-template library.

## Existing repository

1. Inspect Git state, Copier answers, authority/safety, manifests, local policy and both hosts' existing settings.
2. Preserve a clean baseline and old source revision. Generate a separate temporary comparison using native Copier
   with `--skip-tasks`; never copy a new scaffold onto existing product code.
   Guidance-only native adoption never runs the new-project installation task.
3. Merge project routing/docs and activation settings deliberately. Preserve unrelated plugins, permissions and
   custom roles. Integrate generated `.agents/README.md` into the preserved root authority.
4. Confirm the host's registered index matches the expected team identities, or deliberately configure a reviewed
   project Git source. Generated true/false flags are not proof of installation/loading.
5. Complete actual Copier enrollment with retained answers/revision for later tracking. Manually copying comparison
   files does not establish Copier update ownership.

Old local/dual-delivery drafts, earlier `src/apps` layouts and retired inputs require reviewed re-enrollment, not an
in-place mode override or automatic folder migration.
Legacy `/.agents/templates` is excluded from managed deletion. Preserve local adaptations; explicitly review any manual
retirement after checking the replacement Common assets and host loading. No automatic retirement, reinstall,
adaptation recovery or product-code conversion is promised.

For enrolled projects, follow [Copier updates and preservation](updates.md#copier-updates-and-preservation). Shared plugin
releases refresh through the host instead. Credentials, caches, personal trust and live hardware defaults are never
template inputs.
