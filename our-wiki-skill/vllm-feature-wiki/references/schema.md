# vLLM Feature Wiki Schema

## Required Feature README Sections

Every subsystem `README.md` should include:

```text
# Feature: <name>
## Mental Model
## One-Request Story
## State Ledger
## Common Bug Stories
## Related Bugs
## Fuzzer Strategy
## Verification Strategy
## Evidence Sources
## Unknowns
```

Use a state-machine voice. Explain what state is created, mutated, cached/reused, freed, and can become inconsistent.

## State Ledger Shape

Use a table when possible:

```markdown
| State | Created | Mutated | Cached/Reused | Freed | Can Become Inconsistent |
| --- | --- | --- | --- | --- | --- |
```

## Confidence Levels

| Level | Meaning |
| --- | --- |
| verified | Backed by local evidence plus official docs/code or a reproduced local artifact. |
| source-reported | Backed by issue/PR/docs but not locally reproduced. |
| inferred | Reasonable synthesis across sources; label as inference. |
| unknown | Evidence missing. |

## Evidence Basis

Prefer:

1. Local reproduction logs, CI reports, fuzzer history.
2. Local bug capsules and project docs.
3. Official vLLM/vLLM-Ascend docs.
4. GitHub issues, PRs, code diffs, RFCs.
5. Papers.
6. Blogs/Zhihu/general web as supplemental intuition only.

## Cross-Link Rules

- Link feature pages to bug capsules where local capsules exist.
- Link bug-pattern pages and fuzzer playbooks when the feature is fuzzable.
- Keep relative links from the wiki root.
- Do not link to non-existent local pages.

## Quality Gates

- All feature folders have `README.md`.
- `README.md`, `INDEX.md`, and `theory_illustrations/README.md` link major deep dives.
- No legacy model-volume path references.
- New model-path examples use `/mnt/data2/model_weights`.
- Unknown facts remain `unknown`.
