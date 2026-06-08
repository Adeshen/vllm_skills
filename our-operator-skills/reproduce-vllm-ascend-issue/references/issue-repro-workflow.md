# Issue Reproduction Workflow on `npu4`

## Default targets

- repo: `vllm-project/vllm-ascend`
- host: `npu4`
- report dir: `discussion_reports/bug/`

## Step 1: Fetch issue context

Read the issue body and comments first. Extract:

- vLLM / vLLM-Ascend version
- image or wheel assumptions
- hardware and topology
- model family and quantization
- startup command
- workload settings
- exact error signature

Then look for linked or obviously related PRs if the failure smells like a known bug.

## Step 2: Classify reproduction feasibility

Choose one of these paths:

- direct reproduction: current `npu4` environment can match the issue closely
- approximate reproduction: issue must be adapted to local models, topology, or context limits
- blocked reproduction: essential hardware, model assets, or software versions are unavailable

If approximation is required, preserve the fault axis and minimize unrelated changes.

Examples of acceptable approximations:

- same quantization and scheduling flags, smaller model
- same prefix-cache / async / long-context axis, reduced prompt length
- same speculative decode method, closest available target/draft pair

## Step 3: Execute on `npu4`

Use the existing operational patterns:

- runtime setup from the `run-vllm-ascend-docker` skill
- benchmark path from the `benchmark-vllm-ascend` skill
- trace path from the `collect-vllm-ascend-traces` skill when needed

Do not invent a new environment if the current one can test the issue.

## Step 4: Distinguish target fault from local blocker

Before concluding, classify whether the observed failure is:

- the target issue itself
- a known local blocker that fired earlier
- an unrelated runtime or environment failure
- a clean non-reproduction

This matters for cases where a known local issue such as `draft_model` shape mismatch prevents reaching the intended target path.

## Step 5: Write the report

Report path convention:

```text
discussion_reports/bug/issue_<number>_<slug>.md
```

Required sections:

- target issue
- original conditions
- local environment
- chosen reproduction plan
- commands used
- observed result
- conclusion

Recommended conclusion wording:

- `reproduced`
- `approximately_reproduced`
- `not_reproduced`
- `blocked`

## Existing report references

Use these as style references:

- `discussion_reports/bug/issue_8000_approx_fault_injection.md`
- `discussion_reports/bug/vllm_0.18_draft_model_spec_decode_analysis.md`
- `discussion_reports/2026-04-07 vllm-ascend bug watch.md`

## Practical defaults

- If the issue includes a long serve command, preserve only the flags that define the failure axis.
- If the issue depends on unavailable A3 or large-model topology, downshift to the nearest `npu4` equivalent and label it approximate.
- If the service must be started first, verify `/mnt/data`, Docker, and `/v1/models` before load.
- If the issue is benchmark-driven, record artifact paths exactly.
