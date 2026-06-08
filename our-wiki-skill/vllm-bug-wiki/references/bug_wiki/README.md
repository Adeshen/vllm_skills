# vLLM-Ascend Bug Wiki

This wiki is an evidence-driven index over vLLM-Ascend bug research artifacts. It is meant to connect:

```text
bug issue -> failure symptom -> triggering workload -> affected version/image
-> dependency context -> fixing PR/code diff -> patch applicability
-> before/after reproduction evidence -> fuzzer discoverability
```

The wiki is a construction layer only. It links back to source evidence and records unknowns explicitly instead of inventing missing commands, versions, CANN compatibility, or reproduction results.

## Use Cases

For issue triage, start with [INDEX.md](INDEX.md), then open the relevant capsule under [bug_capsules/](bug_capsules/). The `Failure Summary`, `Triggering Workload`, and `Fix Evidence` sections identify whether a report is likely request-triggered, environment-triggered, or patch-validation work.

For patch verification, compare the capsule's `Patch applies to affected commit` field with [release_matrix/README.md](release_matrix/README.md). When no official fixed image is proven, treat the listed derived image as a synthetic verification target, not as a release artifact.

For fuzzer seed design, use the capsule's `Fuzzer Discoverability` section and the workload pattern notes in [workload_patterns/](workload_patterns/). KV/prefix/scheduler/lifecycle cases are the best first GRIEF targets; semantic quality and hardware-specific cases need stronger oracles or environment campaigns.

For release/image selection, use [release_matrix/README.md](release_matrix/README.md) and the upstream release mapping doc. Avoid guessing source commits from Quay tags unless source labels have been inspected.

For CI and local reproduction, use [ci_and_environment/README.md](ci_and_environment/README.md). New NPU work should use `/mnt/data2/model_weights`; do not copy legacy model-volume paths from historical logs into new commands.

## Evidence Policy

- `strong_linked_pr` evidence is suitable for initial benchmark and wiki inclusion.
- `weak_reference` evidence is supporting context only until PR diff or maintainer discussion confirms the fix.
- Open PRs are useful as bug-pattern evidence but should not be described as fixed.
- Missing reproduction, patch-apply, or dependency facts must remain `unknown`.
