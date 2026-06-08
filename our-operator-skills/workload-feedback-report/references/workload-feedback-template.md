# Workload Feedback Report Template

Use this as the canonical structure for the paper-facing workload feedback report.

## Section Order

### `Summary`

Include:

- paper theme
- top family in the current round
- one-sentence state of the search

### `Family Leaderboard`

Use a compact table.

Recommended columns:

| Family | Signal strength | Evidence quality | Current action |
| --- | --- | --- | --- |

### `Per-Family Findings`

Create one subsection per workload family.

Each family subsection must include:

- generation goal
- strongest structured signals
- strongest supporting reports
- caveats or disagreements
- current interpretation
- next generator action

### `Cross-Family Comparison`

Explain:

- which family is strongest for the main paper story
- which family is stable but secondary
- which family is still blocked or appendix-only

### `Next Generator Actions`

Use only these action labels:

- `expand`
- `zoom`
- `freeze`
- `prune`

Each action should say:

- target family
- target axis
- why this action follows from the evidence

### `Evidence Index`

List the concrete runs and reports used.

Recommended format:

- `run`: `id` -> path
- `report`: `id` -> path
- `note`: `id` -> path

## Style Rules

- Main body must be family-centered, not issue-centered.
- Use issue IDs only as supporting evidence tags.
- Prefer explicit conflict notes when structured metrics and narrative reports disagree.
- Keep conclusions modest when evidence is only approximate or environment-specific.
