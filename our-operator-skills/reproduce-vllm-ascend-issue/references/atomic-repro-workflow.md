# Atomic Repro Workflow

This reference turns the `vllm-ascend` issue reproduction process into a labeled execution graph for `npu4`.

## Main Skill

- `reproduce-vllm-ascend-github-issue`

This main skill orchestrates 8 micro-skills and composes atomic operations instead of relying on free-form procedural prompts.

## Micro-Skills

1. `issue-intake`
2. `workspace-and-asset-discovery`
3. `remote-access-and-context-probe`
4. `runtime-and-container-inspection`
5. `service-control-and-readiness`
6. `workload-trigger-and-observation`
7. `evidence-capture-and-classification`
8. `report-solidification`

The source of truth for these stages is `issue_tracker/data/steps.json` and `issue_tracker/data/micro_skill_catalog.json`.

## Atomic Rules

Treat a step as an atom only if it has:

- one clear intent
- one primary input
- one observable output
- a success/failure condition
- reusable semantics across multiple issues

Examples of atoms:

- `tmux capture-pane -t ...`
- `tmux send-keys -t ...`
- `ssh npu4 'docker ps ...'`
- `docker image inspect ...`
- `curl /health` or `/v1/models`
- `rg -n ...`
- `sed -n ...`

Examples of non-atoms that belong in SOP fragments:

- `sleep N && tmux capture-pane ...`
- `docker save ... | ssh npu4 'docker load'`
- `interrupt -> wait -> capture`
- `start service -> sleep/poll -> health probe`

## Required Labels

Each atom must carry:

- `stage`
- `object`
- `intent`
- `cost`
- `fault_role`
- `evidence_shape`

Do not execute or record a step as a reusable atom without those tags.

## Standard Outputs

Use these files as stable interfaces:

- `issue_tracker/data/atom_catalog.json`
- `issue_tracker/data/micro_skill_catalog.json`
- `issue_tracker/data/issue_repro_card.template.json`
- `issue_tracker/data/sop_fragments.json`
- `issue_tracker/data/atom_execution_log.jsonl`

## First-Pass Composition Strategy

Prefer:

1. `low_cost_intake`
2. `remote_scene_probe`
3. `interrupt_then_reobserve`
4. `service_readiness_loop`

Only enter restart-heavy or model-load-heavy paths after `decide_direct_vs_approx_repro` and the runtime inspection atoms both justify it.
