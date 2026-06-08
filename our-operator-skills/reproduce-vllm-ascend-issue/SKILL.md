---
name: reproduce-vllm-ascend-issue
description: Read and reproduce vllm-ascend GitHub issues on npu4. Use when Codex needs to fetch a GitHub issue by URL or issue number, extract the reported environment and failure signature, choose a direct or approximate reproduction on npu4, execute the repro workflow with the existing vLLM Ascend and benchmark toolchain, and write a local Markdown report with a clear reproduction conclusion.
---

# Reproduce vLLM Ascend Issue

Treat issue reproduction as a structured workflow: fetch the issue, extract its repro axes, map them to the current `npu4` environment, run the closest safe reproduction, and write a local report with a precise conclusion.

## Golden Rules

- Extract the issue first; do not start by guessing a command.
- Preserve direct vs approximate reproduction as a first-class distinction.
- Read [../shared/upstream-routes.md](../shared/upstream-routes.md) when selecting companion routes for vLLM serving, benchmark, NCU, FlagOS, NVIDIA distributed/MoE, or evaluation work.
- If a local blocker fires before the target bug, classify the run as blocked or approximate, not reproduced.

## Workflow

1. Fetch and summarize the issue first.
Accept either a GitHub issue URL or an issue number. Default repository is `vllm-project/vllm-ascend`.

2. Extract the real reproduction requirements.
Pull out:
- version and image assumptions
- model path or model family
- topology and device assumptions
- serve command
- workload shape
- exact failure signature
- linked PRs or obvious known fixes

3. Decide direct vs approximate reproduction.
If the issue does not match `npu4` exactly, choose the nearest feasible approximation and say so explicitly in the report.

4. Execute the repro through the existing `npu4` workflows.
Reuse the current Docker, benchmark, and trace operating patterns instead of inventing a one-off path.

5. Record the result locally.
Always write a Markdown report under `discussion_reports/bug/` and classify the outcome.

6. Label the work as atoms and micro-skills.
Before treating any step as reusable, map it to the atomic workflow catalog and log the chosen atom path.

## Standard Inputs

Treat these as the skill inputs:

- issue URL or issue number
- optional repository override
- optional strict reproduction request
- optional trace collection request

Default repository:

- `vllm-project/vllm-ascend`

Default execution environment:

- host: `npu4`
- container: `vllm_qwen3`
- report directory: `discussion_reports/bug/`

## Reproduction Policy

Use these fixed outcome labels:

- `reproduced`
- `approximately_reproduced`
- `not_reproduced`
- `blocked`

Apply them conservatively:

- `reproduced`: materially matching trigger path and failure class
- `approximately_reproduced`: closest feasible `npu4` reproduction hit the same family but not the exact original environment or signature
- `not_reproduced`: service stayed healthy or only unrelated degradation appeared
- `blocked`: required topology, hardware, image, or assets are unavailable

If a known local bug triggers before the target issue, report that separately rather than claiming success.

## Execution Path

Prefer this order:

1. GitHub issue fetch and issue/PR context
2. local asset discovery and prior report review
3. remote scene probe and runtime inspection
4. runtime setup using the `npu4` Docker and model workflow
5. benchmark or direct request workload, depending on the issue
6. trace collection only when the issue involves timing, export, scheduling, or observability ambiguity
7. report writing and atom-path solidification

Use the concrete decision rules and report shape in [references/issue-repro-workflow.md](references/issue-repro-workflow.md).
Use the labeled atom and micro-skill model in [references/atomic-repro-workflow.md](references/atomic-repro-workflow.md).

## Reporting

The final report should include:

- issue link and title
- original reported environment
- chosen `npu4` reproduction or approximation
- exact commands used
- artifact paths
- observed signature
- final conclusion label

## Evidence Contract

Every reproduction claim needs the issue source, extracted trigger axes, local environment, exact command or request, observed result, and artifact path. If any of these are missing, use `blocked` or `approximately_reproduced` rather than a stronger label.

Short session summaries should include:

- whether the issue was reproduced, approximately reproduced, not reproduced, or blocked
- the key signature observed
- the report path
- the chosen atom path or validated SOP fragment when one was confirmed
