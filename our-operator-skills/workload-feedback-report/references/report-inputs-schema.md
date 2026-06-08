# Report Input Schema

Use a single JSON file to define the reading boundary for `workload-feedback-report`.

## Purpose

The bundle prevents the agent from wandering through unrelated notes and mixing evidence accidentally.

## Required Top-Level Fields

### `report_id`

Short identifier for the output report.

Example:

```json
"report_id": "wf-20260428-r1"
```

### `paper_theme`

One-sentence paper focus.

Example:

```json
"paper_theme": "workload generation strategy guided by quantitative anomaly feedback"
```

### `families`

List of workload families that the report should cover.

Each item should include:

- `id`
- `title`
- `goal`
- `primary_axes`
- `issue_tags`

### `runs`

List of structured run summaries. Each item should include:

- `id`
- `family_id`
- `summary_json`
- optional `summary_md`
- optional `requests_csv`
- optional `metrics_csv`
- optional `notes`

### `reports`

List of normalized Markdown reports. Each item should include:

- `id`
- `family_id`
- `path`
- `status`

`status` should be one of:

- `strictly reproduced`
- `approximately reproduced`
- `blocked`
- `environment-specific`

## Optional Fields

### `notes`

Extra supporting notes such as methodology or family interpretation notes.

Each item should include:

- `id`
- `family_id`
- `path`
- `purpose`

### `baselines`

Optional baseline runs used for comparison.

Each item should include:

- `id`
- `version`
- `summary_json`

### `scope_comment`

Optional short note explaining what is intentionally excluded.

## Example Reading Policy

The skill should only read:

- files listed in `runs`
- files listed in `reports`
- files listed in `notes`
- files listed in `baselines`

If a needed source is missing from the bundle, say so explicitly instead of broadening the search.
