---
name: workload-feedback-report
description: Synthesize multiple vLLM Ascend experiment runs and normalized issue reports into a workload-family-centered paper-facing feedback report. Use when Codex needs to compare evidence across runs, rank workload families, and propose the next workload generation actions.
---

# Workload Feedback Report

Treat this skill as a paper-facing synthesis workflow, not a benchmark parser.

The core split is:

- scripts and recorder outputs provide structured evidence
- normalized reports provide contextual interpretation
- this skill turns both into a workload-family feedback report

Do not try to infer the full story from one source type alone.

## Standard Inputs

Use an explicit input bundle. Prefer a JSON file such as `report_inputs.json` over free-form path discovery.

Required input categories:

- `report_id`
- `paper_theme`
- `families`
- `runs`
- `reports`

Optional but recommended:

- `notes`
- `baselines`
- `scope_comment`

Read the exact input shape in [references/report-inputs-schema.md](references/report-inputs-schema.md).

## Workflow

1. Read the input bundle first.
Do not start by scanning the whole repo. The bundle is the reading boundary.

2. Build the evidence table.
For each run, extract only stable hard-evidence fields:
- success rate
- timeout or failure counts
- latency and TTFT
- throughput
- waiting and running pressure
- KV pressure
- preemptions
- prefix-cache query and hit deltas when present

3. Read the normalized reports next.
Use issue or experiment reports to explain:
- what the run was trying to test
- whether the result was strict, approximate, blocked, or environment-specific
- what caveats apply

4. Aggregate by workload family, not by issue.
Each family section must answer:
- what generation goal this family targets
- what anomaly signals were actually observed
- what evidence is strongest
- what the likely boundary or crossover region is
- what the next generator action should be

5. Produce the paper-facing report.
Use the canonical section order in [references/workload-feedback-template.md](references/workload-feedback-template.md).

## Output Rules

The report must be organized by workload family.

Do not structure the main body as:

- issue-by-issue recap
- chronological notebook dump
- one-run-at-a-time summaries

Instead, each family should synthesize across runs and cite issue reports only as supporting evidence.

## Evidence Rules

- Treat `summary.json` and selected metric deltas as hard evidence.
- Treat normalized Markdown reports as contextual interpretation.
- If the two disagree, explicitly mark the disagreement instead of silently resolving it.
- Do not overstate `approximately_reproduced` as a general result.
- Keep issue IDs as evidence tags, not the main organizing principle.

## Required Labels

When describing evidence strength inside the report, use these exact status terms when relevant:

- `strictly reproduced`
- `approximately reproduced`
- `blocked`
- `environment-specific`

For generator actions, use only:

- `expand`
- `zoom`
- `freeze`
- `prune`

## Expected Output

The final response should include:

- report path
- the top workload family
- the most important next generator action

