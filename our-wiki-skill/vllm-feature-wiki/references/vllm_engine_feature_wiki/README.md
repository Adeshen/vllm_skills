# vLLM Engine Feature Wiki

This wiki documents vLLM and vLLM-Ascend engine features as stateful systems. It is the companion to the [bug wiki](../bug_wiki/README.md): the bug wiki records where vLLM-Ascend failed, while this feature wiki explains which engine state made those failures possible.

The main use cases are:

- Bug digging: turn symptoms into scheduler, cache, request, sequence, distributed, metrics, and backend state hypotheses.
- Fuzzer design: turn feature state transitions into seeds, mutation axes, oracles, and monitors.
- vLLM-Ascend verification: choose smoke tests and before/after checks that match the feature state being patched.
- Release triage: connect feature risk to patch bases, images, and environment constraints.

All pages are evidence-driven. If a feature detail, command, version, or compatibility fact is not present in local evidence, it is recorded as `unknown`. New model-path examples must use `/mnt/data2/model_weights`.

## Reading Path

Start with [INDEX.md](INDEX.md) to find the subsystem. Each feature page now follows the same teaching path:

1. Mental model.
2. One-request story.
3. State ledger.
4. Common bug stories.
5. Fuzzer and verification strategy.
6. Sources and unknowns.

For cross-feature issues, use [feature_to_bug_map/README.md](feature_to_bug_map/README.md). For official feature coverage from vLLM-Ascend documentation, use [OFFICIAL_FEATURE_COVERAGE.md](OFFICIAL_FEATURE_COVERAGE.md).

## Theory Layer

Use [theory_illustrations/README.md](theory_illustrations/README.md) when the subsystem concept itself is unclear. It links the narrative pages below:

- [GLOSSARY.md](theory_illustrations/GLOSSARY.md)
- [STATE_INVARIANTS.md](theory_illustrations/STATE_INVARIANTS.md)
- [FUZZER_PLAYBOOKS.md](theory_illustrations/FUZZER_PLAYBOOKS.md)
- [BUG_READING_WORKFLOW.md](theory_illustrations/BUG_READING_WORKFLOW.md)
- [SCHEDULER_DEEP_DIVE.md](theory_illustrations/SCHEDULER_DEEP_DIVE.md)
- [KV_CACHE_DEEP_DIVE.md](theory_illustrations/KV_CACHE_DEEP_DIVE.md)
- [ATTENTION_DEEP_DIVE.md](theory_illustrations/ATTENTION_DEEP_DIVE.md)
- [SAMPLING_AND_SPEC_DEEP_DIVE.md](theory_illustrations/SAMPLING_AND_SPEC_DEEP_DIVE.md)
- [STREAMING_LIFECYCLE_DEEP_DIVE.md](theory_illustrations/STREAMING_LIFECYCLE_DEEP_DIVE.md)
- [PD_MOONCAKE_DEEP_DIVE.md](theory_illustrations/PD_MOONCAKE_DEEP_DIVE.md)
- [QUANT_MOE_DEEP_DIVE.md](theory_illustrations/QUANT_MOE_DEEP_DIVE.md)
- [ASCEND_BACKEND_DEEP_DIVE.md](theory_illustrations/ASCEND_BACKEND_DEEP_DIVE.md)
- [SOURCE_NOTES.md](theory_illustrations/SOURCE_NOTES.md)

## Companion Sources

- [Bug wiki](../bug_wiki/README.md)
- [Fuzzer findability](../bug_wiki/fuzzer_findability/README.md)
- [Release matrix](../bug_wiki/release_matrix/README.md)
- [CI and environment](../bug_wiki/ci_and_environment/README.md)
