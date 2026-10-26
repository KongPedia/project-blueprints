# Updating shared plugins and product guidance

| Change | Update channel | Review boundary |
| --- | --- | --- |
| Shared procedures, blank forms/resources and host adapters | Registered skills index and plugin release | Source/provenance/license review, host refresh and fresh-session checks |
| Product routing, docs and activation | Copier update | Per-project diff, unrelated settings, local policy and preservation checks |
| Product code/dependencies/runtime config | Native package change | Package tests, compatibility and deployment authority |

Root `docs/` describes maintaining the template and is not copied. Product-local contracts and decisions stay local;
shared methods, blank forms and worked references stay with installed Common/robotics skills, not copied manuals.
There is no local skill mirror/sync pipeline, preset-answer directory or second procedure catalog here.

## Host-owned source

By default projects record activation flags only and each host owns its registered local/private index. See
[source selection](adoption.md#plugin-source-selection), provider host setup (`agent-skills/docs/hosts.md`) and
shared releases, refresh and recovery (`agent-skills/docs/releases.md`) for the canonical host/release procedures.
Pushing a tag does not refresh hosts or reload sessions; host caches are not independent per-project version locks.
Local checks alone do not establish private authentication, hosted releases or App/Claude discovery.
The new-project copy task installs selected Codex identities only from the already registered host source with an empty
project repository and reviewed native Copier task authorization (`--trust`). `--skip-tasks` renders without installation.
Native copy can merge existing directories; always use a new destination for generation. Nonempty advanced repositories
are rejected before any add. Source/ref changes can still reuse a
stale same-name Git cache; review actual source/bytes rather than treating configuration as retargeting proof. The task
does not replace shared release refresh or install during guidance adoption/updates. Manual commands remain recovery
and Claude alternatives.

## Copier updates and preservation

An answers file or `_commit` value alone is not durable enrollment: the recorded old template commit must actually
exist and remain accessible from the recorded source. An uncommitted source without retained Git revisions can leave
only an unavailable temporary revision. Treat that output as a prototype; long-lived adoption needs an authorized
versioned source baseline and reviewed fresh re-enrollment preserving product code and local policy. Do not rewrite
answers, initialize/commit/tag Git or convert the source automatically to manufacture update readiness.

On a clean review branch with committed history, recorded answers and the prior source revision available:

```bash
uvx copier update --trust --skip-tasks --vcs-ref '<reviewed-template-revision>'
```

Review both template revisions before authorizing `--trust`. Copier 9.19.1 can require it on update because the old
template declares tasks, even with `--skip-tasks` and a copy-only condition. The current installation task does not run
on update; `--skip-tasks` also explicitly suppresses tasks. This is not Codex workspace/hook trust or permission to
reconfigure personal host state.
Native Copier has no extra installation-confirmation or new-destination guard; review commands and targets explicitly.

Review conflicts/deletions, commands/authority and source/selection settings; preserve unrelated plugins, permissions
and custom policy. Maintainer root docs are not update payloads.
Product source/manifests/configuration, tests/scripts/bin and root README are seed-only. Changing a profile does not
migrate its product behavior; compare a fresh generation and adopt native changes separately.

Earlier local/dual-delivery drafts need reviewed re-enrollment, not automatic retirement or an override. Preserve local
adaptations, compare a fresh generation and confirm replacement host loading before explicitly removing duplicates.
Legacy `/.agents/templates` is explicitly excluded from managed deletion, including customized forms and user-added
files. New projects receive no generic form copies. Inspect the shared replacement assets and local changes before
an explicit reviewed manual retirement; moving an asset into a plugin never authorizes deleting a consumer copy.
An update does not reinstall plugins, recover customizations or prove session loading. Never force/reset other work
to hide conflicts.

A future fleet rollout can propose reviewed configuration PRs where selection changes while hosts refresh already
selected shared bundles. Batch automation, organization-wide host administration and publication are not generation
features. Optional hooks remain off unless selected and separately trusted; they never authorize tests/apps/hardware.
