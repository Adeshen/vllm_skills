# Feature: <name>

## Mental Model
Explain the feature as a state machine. Name the central state object, who owns it, and why it exists.

## Why This Feature Exists
Explain what user or engine problem the feature solves.

## One-Request Story
Walk through one request from arrival to cleanup:

1. Request enters:
2. Scheduler admits:
3. Feature state is created:
4. Forward/sampling/transfer work happens:
5. Output is emitted:
6. Cleanup frees or preserves state:

## State Ledger

| State type | What is created | What is mutated | What is cached/reused | What is freed | What can become inconsistent |
| --- | --- | --- | --- | --- | --- |
| Scheduler state |  |  |  |  |  |
| KV/cache state |  |  |  |  |  |
| Request/output state |  |  |  |  |  |
| Distributed state |  |  |  |  |  |
| Metrics/backend state |  |  |  |  |  |

## User-Facing Inputs
- API parameters:
- Model config:
- Runtime flags:
- Environment variables:

## Ascend-Specific Notes
Explain how vLLM-Ascend changes or constrains this feature. Use `unknown` where the local evidence does not prove a claim.

## Common Bug Stories
Describe common failure stories as state transitions that went wrong.

## Related Bugs
Link to bug capsules or known issues.

## Fuzzer Strategy
- Seed shape:
- Mutation axes:
- Oracle:
- Monitor:
- Expected failure signals:

## Verification Strategy
- Unit tests:
- Integration tests:
- Smoke tests:
- Reproduction commands:

## Theory Links
- Deep dive:
- State invariants:
- Fuzzer playbook:
- Feature-to-bug map:

## Evidence Sources
List source files, docs, issue links, logs, reports, or local wiki pages used.

## Unknowns
List missing evidence.
