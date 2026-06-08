---
name: record-vllm-ascend-report
description: Normalize vLLM Ascend experiment, benchmark, trace, and GitHub issue reproduction notes into consistent Markdown reports. Use when Codex needs to turn raw logs, commands, metrics, or free-form notes into a structured report under discussion_reports/bug with fixed sections, conclusion labels, artifact naming, and concise next steps.
---

# Record vLLM Ascend Report

Turn raw execution notes into a report that is easy to compare across runs. Keep the structure fixed, preserve the difference between original issue conditions and local observations, and avoid ad hoc section drift.

## Golden Rules

- Reports normalize evidence; they do not upgrade weak evidence into stronger conclusions.
- Keep original issue conditions, local approximation, commands, artifacts, and interpretation separate.
- Read [../shared/upstream-routes.md](../shared/upstream-routes.md) when a report mentions upstream vLLM, NCU, NVIDIA, FlagOS, or evaluation skill routes.
- Every conclusion label must be justified by a concrete signature or blocker.

## Workflow

1. Identify the report type first.
Decide whether the input is:
- issue-driven reproduction
- local experiment or benchmark
- trace or observability investigation

2. Gather the minimum facts needed for a normalized report.
Pull out:
- target issue or experiment topic
- local environment
- case matrix or key variants
- exact commands used
- observed metrics and failure signatures
- artifact paths
- concrete next steps

3. Use the canonical section order.
Keep the report in this order:
- `Target`
- `Original Conditions`
- `Local Environment`
- `Experiment Matrix`
- `Commands Used`
- `Observed Results`
- `Conclusion`
- `Next Steps`

Omit `Original Conditions` only when the report is not tied to a GitHub issue or external target.

4. Apply normalized labels.
Use these conclusion labels exactly:
- `reproduced`
- `approximately_reproduced`
- `not_reproduced`
- `blocked`

Use these failure-source labels when helpful:
- `target_issue`
- `local_blocker`
- `environment_mismatch`
- `benchmark_plumbing`
- `performance_only`

5. Write or update the report in the canonical location.
Default to `discussion_reports/bug/`. Prefer updating an existing matching report over creating a near-duplicate.

## Naming Rules

- issue-driven: `discussion_reports/bug/issue_<number>_<slug>.md`
- experiment-driven: `discussion_reports/bug/<topic>_<yyyymmdd>.md`

Slug rules:

- lowercase
- hyphen-separated
- concise fault or topic phrase
- no unnecessary timestamps or model hashes in the slug

## Artifact Naming

Use fixed artifact categories in the report when listing evidence:

- `service_log`
- `evalscope_log`
- `evalscope_outputs`
- `kv_csv`
- `kv_log`
- `trace_query`
- `trace_ui`

## Reporting Rules

- Keep the report factual and compact.
- Separate original issue conditions from local approximation.
- If a local blocker fires before the intended bug, say that explicitly instead of overstating reproduction success.
- Keep exact commands and artifact paths verbatim.
- Keep interpretation short inside `Conclusion`; move follow-up work to `Next Steps`.

Use the concrete section shape and wording guidance in [references/report-template.md](references/report-template.md).

## HTML Report Generation

After writing the markdown report, also generate an HTML report:

1. Use the `/update-issue-tracker` skill for detailed HTML generation guidance
2. Read the template at `issue_tracker/templates/issue_report_template.html`
3. Convert each markdown section to HTML following the conversion guide
4. Replace all placeholders in the template
5. Save the HTML file to `discussion_reports/bug/issue_{{id}}_{{slug}}.html`

See `../update-issue-tracker/references/html-generation-guide.md` for detailed conversion examples.

## Update Tracker State

After generating reports, update the issue tracker state:

1. Update `issue_tracker/data/issues.json` with current issue status
2. Set the `html_report_path` field to the generated HTML file
3. Update progress statistics in the `metadata` section
4. Update the `summary` section with overall statistics

## Expected Output

The final response should include:

- the report path (markdown)
- the HTML report path
- the normalized conclusion label
- the primary observed signature
