# Project Blueprints maintainer contract

## Scope and ownership

This repository owns native Copier scaffolds and project-specific plugin integration, not reusable skill bodies.
`agent-skills` owns the canonical procedures, resources, licenses, hooks and generic role sources. Neighboring
BattleBang/ESP/Unitree repositories are read-only reference inputs. Private releases require explicit authorization;
public distribution additionally requires a license and proprietary-scope review.

- Read this contract and the owning source/readme. Use relevant organization plugin procedures; when
  maintaining an unpublished local source, inspect the exact applicable canonical procedure in the sibling
  `agent-skills/source/.agents/skills` checkout. Do not create another procedure mirror here.
- `copier.yml` owns questions, derived selection, validation and update boundaries. `blueprints/profiles.json` owns
  native profile/component-to-plugin identity mapping. `template/` owns output files and assembles native `blueprints/`
  fragments through internal symlink mounts. Root `docs/` is maintainer-only. Actual product routing, specs/ADRs and
  design briefs stay local; reusable blank forms and methodology belong to shared skills, not generated `.agents/templates`.
- Plugin IDs are a shared public contract, not copies of the central skill inventory or implementation. Validate them
  against the reviewed central catalog when both sources are available. A trusted native Copier copy task installs
  only the selected Codex plugin union; no shared skill bodies, installer wrapper or cache enter the product.
- Generic agent definitions are owned centrally. Codex does not load custom-agent TOMLs from plugins in the verified
  clients; use built-in agents by default, or explicitly provision native project-owned specialization separately.

## Execution and authority

- Follow the latest user scope. Execute clear reversible work; do not repeat granted approvals or widen authorization.
- Inspect affected source, callers, fixtures and output before changes. Keep profile questions and rendering in native
  Copier. Do not add another CLI, wizard, copied Markdown library or submodule. Native post-copy Codex provisioning is intentional;
  preserve Copier task authorization, fail on installation errors and never silently use a different explicit source.
- Independent bounded tasks may use native subagents with explicit file ownership and evidence requirements. You are
  not alone: preserve others' edits and coordinate shared registry/config changes through one integration owner.
- Do not copy host caches, credentials, auth, sessions, trust or absolute host paths. Internal source-relative symlinks
  are intentional assembly; generated projects must contain ordinary files.
- Project trust, plugin installation/activation, hook trust and actual agent discovery are different claims. Do not
  fabricate unsupported manifest fields or interpret configuration as execution/adherence evidence.
- Host plugin installation is host-scoped and may enable bundles globally; project flags require native project trust.
  Never auto-grant project/hook trust, retarget registered sources, uninstall unrelated plugins or run tasks on updates/adoption.
- Native Copier permits existing-directory merges. New generation must use a new destination; never promise an
  automatic existing-path abort or installation-confirmation prompt. `--trust` authorizes reviewed template execution;
  `--skip-tasks` renders without installing. Neither approves Codex workspace/hook trust.
- No commits, remotes, tags, pushes, CI dispatch, publishing, services or hardware without corresponding authorization.

## Verification and preservation

- Generator/profile changes require `uv run --locked pytest`, including actual render/selection and temporary Git
  update/adoption preservation checks. Test commits belong only to disposable fixtures, never this user checkout.
- Keep focused boundary tests, not tests of a programming language or duplicated upstream instruction prose. Native
  starter checks prove only their actual package layer. Never contact physical devices or hardware-connected brokers.
- Monorepos group packages at root `apps/` and `packages/`; native package source remains inside each package.
- Preserve product seeds, root authority and unrelated existing host settings on managed guidance updates. Adoption and
  migration require reviewed diffs; do not silently retire customized files or rewrite recorded answers by hand.
- Preserve legacy `/.agents/templates` through the managed exclusion. Remove old copies only through explicit reviewed
  manual retirement after checking local adaptations and replacement shared assets; never automate their deletion.
- Prose-only changes use parsing, local-reference/closure and complete-file diff/whitespace checks; do not launch apps.
- Substantial routing, shared contracts and safety changes require an independent review/evidence pass.
- Report actual checks, omitted layers and rollback. Local static/software evidence is not GitHub delivery, fresh App
  or Claude discovery, model compliance, production readiness, deployment or hardware validation.
