# Template maintainer documentation

These documents explain maintaining and using **the template source**. They are not copied into generated products.
Product-owned guidance is authored once under `template/`; native package READMEs live with `blueprints/` fragments.

| Purpose | Document |
| --- | --- |
| Source/output ownership and directory responsibilities | [Root README](../README.md#source-is-not-the-generated-product) |
| Native generation, automatic Codex installation, adoption and re-enrollment | [Adoption](adoption.md) |
| Local/private plugin indexes and host lifecycle | Shared host setup (`agent-skills/docs/hosts.md`) |
| Plugin releases versus project configuration updates | [Updates](updates.md) |
| Official/upstream references and applicability | [Sources](sources.md) |
| Observed checks and omissions | [Verification](verification.md) |
| Evaluation scope and operational limits | [Evaluation](evaluation.md) |

## Product contracts versus shared procedures

- [Product docs source](../template/docs/) owns product structure and maintained local contracts.
- Filled [specifications](../template/docs/specs/README.md), [ADRs](../template/docs/adr/README.md) and the
  [design brief](../template/DESIGN.md) stay project-owned.
- TDD/SDD/selective DDD, source-first investigation, architecture and robotics worked references belong to their
  installed common/robotics skills. Follow those procedures' packaged references; do not copy another manual here.
- Generic blank task/spec/README forms and the ADR format are shared Common assets, not Copier output.

`AGENTS.md` governs template maintenance. Generated authority, commands, specs and local policy belong to the consuming
project. Shared reusable procedures and their full catalog/resources belong only to `agent-skills`.
File/configuration presence does not prove host loading, model adherence or execution success.
New-project copies install selected Codex plugins only from the already registered host source, with the default empty
project repository and authorized Copier tasks. Advanced source selection is render-only with `--skip-tasks` until
source/cache identity is reviewed manually. Copier task authorization, registration and workspace/hook trust differ.
