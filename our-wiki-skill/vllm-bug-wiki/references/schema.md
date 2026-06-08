# vLLM Bug Wiki Schema

## Required Capsule Sections

Each capsule should follow `BUG_CAPSULE_TEMPLATE.md` and include:

```text
# Bug Capsule: <short name>
## Identity
## Failure Summary
## Triggering Workload
## Version And Environment
## Fix Evidence
## Reproduction Evidence
## Fuzzer Discoverability
## Next Actions
```

## Evidence Status

| Status | Meaning |
| --- | --- |
| complete | Issue, fix, affected/fixed version, reproduction, and fuzzer judgment are all locally supported. |
| strong | Issue and fix are supported; one or more reproduction/version fields may be missing. |
| partial | Some local evidence exists but important links are missing. |
| weak | Mostly issue text or inferred connection. |
| unknown | Evidence missing. |

## Confidence Levels

| Level | Meaning |
| --- | --- |
| high | Local evidence ties issue, failure symptom, fix PR, and affected surface together. |
| medium | Issue and fix are plausible but reproduction/version evidence is incomplete. |
| low | Candidate relation only. |
| unknown | Not enough evidence. |

## Fuzzer Findability

Use:

- `yes`: request-level seed plus oracle/monitor is enough.
- `partial`: needs special environment, backend mode, or instrumentation.
- `no`: startup/dependency/CI-only issue outside request fuzzing.
- `unknown`: evidence missing.

Always record required seed type, oracle, monitor, mutation axes, and why it is or is not fuzzable.

## Quality Gates

- `README.md`, `INDEX.md`, and `BUG_CAPSULE_TEMPLATE.md` exist.
- Every capsule has all required sections.
- `INDEX.md` links high-value capsules.
- No legacy model-volume path references.
- Unknown facts remain `unknown`.
- Local evidence files are not modified during capsule construction.
