# Local verification record

2026-10-26, macOS. Scope: native Copier automatic Codex provisioning, ownership/composition,
reusable form migration and non-destructive updates. This is not hosted delivery, model-adherence or product/hardware certification.

## Complete local gates

| Check | Observed result |
| --- | --- |
| `project-blueprints`: `uv run --locked pytest -q` | **75 passed**, 46.96s (native Copier) |
| `agent-skills`: `uv run --locked pytest -q` | **45 passed**, 4.11s |
| Central builder `--check` | All **308** generated artifacts match canonical sources |
| `scripts/check_plugin_contract.py ../agent-skills` | All **13** plugin IDs and selection dependencies agree |
| Static source/config/link/whitespace checks | Both repositories passed; rendered/plugin link closure also covered |

Tests use disposable roots and never create commits/tags in user checkouts. The separately authorized private release
uses real source history and matching `v0.1.0` tags. Earlier wizard/safety-CLI and pre-cleanup counts are superseded;
the removed CLI's 19 tests and installed-tool checks are not release acceptance evidence.

## Ownership and minimality

- Eight native profiles and seven built-in compositions use native Copier. Single packages keep native `src/`;
  monorepos group complete packages under root `apps/` and selected `packages/`. No empty outer `src` or unused group.
- Ten internal source symlinks remain: eight native mounts plus ignore/PR sources. Output files are ordinary files.
  These assembly aliases are not independently authored copies. Redundant generic `src/README` was removed.
- Fresh output has no `.agents/templates`, reusable skill bodies, copied licenses/catalog, generic role mirrors,
  selection JSON, separate routing file or maintainer manuals. `.agents` contains project routing and setup only.
- Both old five-form source families were removed. Common ships optional task/change assets and one combined
  package/folder README guide under existing skills. Matt's existing ADR format remains byte-identical.
- Product specs/ADR indexes are six-line destination markers; actual filled records remain local. Shared development,
  architecture and robotics references stay in provider skills. Root maintainer docs were consolidated from eight to six.

## Source and release integrity

The inventory remains **41 unique skills / 13 plugins**; the catalog is unchanged. All **197** recorded canonical
file hashes match. Every one of the **186 imported-file records** retains its upstream hash/source identity: **183**
source files are byte-identical to the pre-audit snapshot; only Docs Sync, Writing Plans and Domain Modeling entrypoints
received narrow optional-resource/evidence guidance, with reviewed local hashes. No imported body/resource was removed.

Three original team assets have authored provenance, not invented upstream hashes/licenses. Resources attached to
imported skills are separately recorded under `authored_resources`; the original SDD skill owns its change-spec asset.
Existing recursive packaging closes resources and records source/payload hashes. Tampering with an authored asset
fails before replacing output. License/NOTICE, deterministic generation, symlink/output preflight and role adapters remain checked.

## Actual automatic installation through Copier

Actual raw `uvx copier@latest copy --trust --defaults ... <git+file://source> <target>` ran against a disposable tagged
source with a pre-registered local provider. Each case had fresh HOME/CODEX_HOME. **No manual plugin-add commands were
run outside Copier**: its native argv-style Python task called Codex's native installer from the derived profile union.

| Case | Automatically installed bundles |
| --- | --- |
| General Python | Common + Python; no UI/framework bundles |
| Next.js standalone | Common + API contracts + TypeScript + React/UI + Next; no Python |
| Python backend monorepo | Common + Python + API contracts + FastAPI; `apps/api`, `apps/worker`, `packages/domain` |
| Python + React monorepo | Common + Python + API contracts + FastAPI + TypeScript + React/UI |

All four exact installed sets matched. Every installed cache file matched provider bytes, and the full 13-plugin
activation matrix matched selection. No skill/form/plugin bodies were copied into products. Native Codex project/hook
trust was not granted. Copier's current task/config and provider payloads match the fixture; all 16 external fixture
commands exited successfully. Commands resolved to Copier 9.19.1 and Codex 0.160.0.

The task runs only on initial project copy, not guidance adoption or updates. Native Copier task execution needs
`--trust` or a separately trusted template. `--skip-tasks` is render-only in the inspected version; old task-bearing
update metadata can still require trust. Task failure stops provisioning; earlier host installs are not rolled back.
Copier permits existing-directory merges and can clean up a fresh destination on failure. Always use a new destination;
there is no installation-confirmation or existing-path-abort guarantee. Codex installation globally enables selected
plugins; trusted project flags and a fresh session remain separate, not automatic per-folder or version isolation.

The automatic path uses the already registered host source only. It rejects a nonempty advanced repository before
any add. Isolated probes in Codex 0.160.0 and 0.162.0-alpha.17.2 showed that Git URL/ref CLI overrides can reuse a
same-name old snapshot rather than fetch the requested source. No task tries overrides, retargets registration or
repairs caches. Advanced source configuration is render/manual-review only, not a verified fetch or freeze.

## Real consumer audit boundary

The initial single-Python/robotics consumer enabled exactly Common, Python, Robotics and the opt-in Session Guidance;
all four installed caches matched provider bytes, with no UI/Rust/C++/HTTP bundle enabled. A disposable copy passed its
smoke test and entrypoint on Python 3.10/3.13, built a wheel/source archive and imported its independently installed wheel.

Later inspection found the real directory had changed to Litestar/React monorepo answers while earlier root Python
files remained. No new template was rendered there by this audit; only an earlier setup-guide correction was applied.
The changed consumer is not validated as a clean single project. No automatic repair, deletion or answer rewrite was
attempted. Its old recorded template commit is unavailable, so that prototype still requires reviewed re-enrollment;
creating the new source release does not repair its historical answers. The discarded safety-CLI probe was not a
native Copier guarantee and is not part of this release.

## Regression and independent review

Meaningful RED checks reproduced both missing installed form assets and **actual deletion of five old-template form
files, including a consumer customization**, on Copier update. After the permanent legacy-path exclusion, a genuine
Git-backed old-to-new update preserves every legacy form and a user-only file byte-for-byte while applying new routing.
Fresh generation creates no form copies. Existing product/authority/settings preservation and draft re-enrollment
rejection checks also pass. New tests exercise the causal boundary, not duplicated language/upstream prose.

Independent architecture/DevOps and AI-harness reviews inspected the baseline diff, caller closure, authored provenance,
unchanged ADR and update coverage. They found no remaining blocking issue in that scope. A sibling-only documentation
link was corrected to an honest provider locator, without inventing an unpublished URL. Role-model capacity required
an inherited-model reviewer fallback. Reviewers distinguished their own static checks from parent-run suite logs.

Nine provisioning cases cover exact selection/deduplication, trust/render-only boundaries, failure propagation,
advanced-source refusal and update/adoption non-execution. An initial recording fixture changed `os.environ` but not
Plumbum's exported environment; expected installer calls were not captured and native adds failed on the absent
marketplace. No successful personal install/config change was observed. The fixture now isolates PATH, HOME and
CODEX_HOME through `local.env`. A missing `overwrite` in the update fixture was corrected. The first real-install
receipt parser assumed a nonexistent `installedPath` list field; the corrected probe uses actual native printed cache
paths and passed all four cases. These intermediate failures were not counted as successful installation evidence.
Three further meaningful RED failures reproduced missing-CLI and first/later plugin-add errors; corrected task handling
now preserves native errors, gives the one-time registration/render-only hint, stops the chain and avoids Python tracebacks.

## Limits

- These local checks do not establish hosted Git authentication/CI or downstream rollout. Release publication and its
  observed GitHub results are recorded separately in release notes. Cross-repository CI skips without reviewed refs;
  private sibling access needs separately provisioned rights.
- No personal host registration/config/trust changes: installation probes used disposable homes/caches.
- No fresh App/Claude session, model invocation/adherence evaluation or native hook-trust/execution test.
- No HTTP/frontend product dependency installation/build rerun, services/browser/E2E, MCU/serial/broker or hardware.
- Private/team use must still respect source rights. Public publication additionally needs original-material licensing
  and secret/proprietary-scope review; local/private indexes do not require public-directory submission.
