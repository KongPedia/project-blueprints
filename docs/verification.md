# Maintainer verification gates

This page defines reusable checks, not a dated consumer migration receipt. Keep actual command output, host/client
versions, source revisions and omitted layers in the corresponding review/release evidence outside the template payload.
A previous passing check is not evidence that the current diff passes.

## Local source gates

From each reviewed checkout:

```bash
# project-blueprints
uv run --locked pytest
uv run --locked python scripts/check_plugin_contract.py /path/to/agent-skills
git diff --check

# agent-skills
uv run --locked pytest
uv run --locked python scripts/build_plugins.py --check
git diff --check
```

Tests use disposable Git/template/consumer roots. Fixture commits/tags never belong to user checkouts.
Use existing locked dependencies; do not install product dependencies or start applications/hardware to validate prose.

## Required invariants

| Boundary | Evidence to collect |
| --- | --- |
| Profiles/composition | Native render, exact bundle union, complete true/false host matrix; FastAPI **and** Litestar retain shared API contracts |
| Native code seeds | Correct package owner/manifests; Python smoke identifies owned source and executes its real module entrypoint |
| Resource generation | Deterministic output, ordinary-file closure, source/local/payload hashes, retained license/NOTICE; rejected input preserves output |
| Guidance adoption | Actual disposable existing-repository copy; byte-preserved authority, routing/docs, custom roles/resources, settings and gitlinks |
| Managed update | Retained old source revision and clean disposable Git history; protected seeds/policy, conflicts and legacy resources preserved |
| Copy-only provisioning | Recorded argv/output and exact selected set in disposable HOME/CODEX_HOME; errors stop, earlier installs are not silently rolled back |
| Native host support | Effective installed bytes, project selection and fresh discovery tested separately from installation/configuration |

No generated project receives shared skill bodies, generic role mirrors, host caches/auth/trust, reusable blank forms or
maintainer manuals. Internal source assembly symlinks must render as ordinary files. Common assets remain skill-owned.

## Hosted validation and private sibling contract

Normal unprivileged validation runs on pull requests and configured pushes. Optional private cross-repository checks
are **trusted-push-only**: every pull request and an unset ref skip this layer, which means **not verified**.

| Workflow owner | Reviewed full 40-hex sibling commit variable | Read-only token target |
| --- | --- | --- |
| `project-blueprints` | `AGENT_SKILLS_CONTRACT_REF` | private `agent-skills` |
| `agent-skills` | `BLUEPRINTS_CONTRACT_REF` | private `project-blueprints` |

Separately provision `SHARED_REPOSITORY_READ_TOKEN` in each workflow repository. Prefer an expiring fine-grained token
restricted to the sibling with **Contents: read**, or a suitably scoped short-lived GitHub App token. The
[default workflow token is current-repository scoped](https://docs.github.com/en/actions/concepts/security/github_token),
and [checkout documents separate private-repository credentials](https://github.com/actions/checkout#checkout-multiple-repos-private).
SHA syntax is checked, not human review; invalid refs/missing credentials fail before checkout without printing values.
Both checkouts disable credential persistence. Do not expose sibling contents or credentials to untrusted PR scripts.

Observe actual hosted jobs and annotations. Missing runner/billing/access means **blocked**, not a failed software test
or a pass. A skipped contract job is never a successful integration check. Do not dispatch CI, create secrets or alter
account billing without corresponding authority; a local workflow check does not prove hosted delivery.

## Host and update evidence boundaries

Native Copier permits existing-directory merges; use a new destination for generation and a disposable copy before
[guidance enrollment](adoption.md#executable-guidance-only-enrollment). Keep the recorded old source revision accessible;
new source history cannot repair unavailable prototype lineage. Never manufacture `_commit` or erase custom content.

Review source/task/migration definitions before `--trust`. `--skip-tasks` skips regular tasks, not arbitrary migration
tasks. The reviewed template's installation task is copy-only and excluded from guidance adoption/updates; Copier
9.19.1 may still require update trust for prior task metadata. This is not agent workspace/hook trust.

Use disposable HOME/CODEX_HOME for host packaging checks. Compare actual cache bytes, not requested URLs/refs:
same-name source caches can be stale. Do not retarget a real user's registered index or mutate credentials/trust.
Skills are host-managed; a monorepo bundle union is task routing, not per-folder isolation or per-project version locking.

Claude's instruction discovery varies by client version and ancestor authority; the one-line `@AGENTS.md` bridge is a
compatibility import, not a second policy. Static checks do not establish a Claude/App session or model adherence.
Report installation, discovery, relevant-versus-irrelevant invocation, optional hook trust/execution and refresh separately.
No software/configuration result proves production acceptance, successful deployment or physical safety.
