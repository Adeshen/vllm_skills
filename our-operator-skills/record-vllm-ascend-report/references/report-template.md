# Normalized Report Template

Use this as the canonical report shape for `discussion_reports/bug/`.

## Section Order

### `Target`

Include:

- issue link and title, or experiment title
- one-line purpose

### `Original Conditions`

Include only for issue-driven reports.

Capture the original report as stated upstream:

- environment or topology
- model or model family
- serve command or key switches
- workload shape
- failure signature

If the local run is only an approximation, say that here or in `Local Environment`.

### `Local Environment`

Capture the current execution context:

- date
- host
- container or image
- model path and served name
- version or build assumptions
- any known environment mismatch

### `Experiment Matrix`

Use a compact table when multiple cases were run. Recommended columns:

| Case | Port or ID | Key switches | Status |
| --- | --- | --- | --- |

If there was only one case, this section can be a short bullet list instead of a table.

### `Commands Used`

Include exact commands, grouped by purpose:

- environment preparation
- service launch
- benchmark or repro workload
- trace query if used

Prefer fenced code blocks with shell commands exactly as run.

### `Observed Results`

Keep this evidence-first.

Include:

- request counts and success or failure counts when available
- TTFT, TPOT, throughput, or latency when relevant
- exact failure signature
- artifact paths using normalized artifact labels

Recommended artifact formatting:

- `service_log`: `/path/to/service.log`
- `evalscope_log`: `/path/to/evalscope.log`
- `evalscope_outputs`: `/path/to/outputs`
- `kv_csv`: `/path/to/file.csv`
- `kv_log`: `/path/to/file.log`
- `trace_query`: `http://127.0.0.1:16686/api/...`
- `trace_ui`: `http://127.0.0.1:16686/search`

### `Conclusion`

Start with one normalized conclusion label:

- `reproduced`
- `approximately_reproduced`
- `not_reproduced`
- `blocked`

Then keep interpretation short:

- whether the target issue was hit
- whether a `local_blocker` or `environment_mismatch` prevented a strict repro
- whether the run only showed `performance_only` differences

### `Next Steps`

List only concrete next actions. Good examples:

- increase prompt length while holding concurrency fixed
- rerun on a build containing a linked fix
- remove speculative decode to isolate scheduling effects
- collect traces for the failing path

## Style Rules

- Do not invent extra top-level sections unless the user explicitly asks.
- Keep section order fixed.
- Prefer exact commands and exact paths over paraphrase.
- Avoid duplicated interpretation blocks.
- Prefer updating the existing report when the topic is clearly the same.

## Example File Names

- `discussion_reports/bug/issue_8000_long-context-prefix-async.md`
- `discussion_reports/bug/prefix-cache-kv-baseline_20260420.md`
