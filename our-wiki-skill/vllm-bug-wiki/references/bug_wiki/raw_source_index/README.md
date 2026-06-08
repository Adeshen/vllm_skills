# Raw Source Index

This page lists source evidence directories used by the bug wiki. Treat these files as primary evidence and the wiki as a derived index.

## Issue Capsule Root

[../issue_capsule/](../../issue_capsule/) contains the broader vLLM-Ascend research capsule set, environment constraints, workloads, project docs, issue folders, and GRIEF history.

## GitHub Research

[github_research/](../../issue_capsule/github_research/) contains issue inventories, reproduction lists, manual taxonomy worksets, and release summaries.

Important files:

- `vllm_ascend_issues_20260512.md`
- `vllm_ascend_reproduction_list.md`
- `manual_taxonomy_workset_20260512/vllmascend_workload_induced_bugs_highconf.json`

## GitHub Issue HTML/Search Cache

[workloads/github_bug_issue_html_cache_vllm_search_20260519/](../../issue_capsule/workloads/github_bug_issue_html_cache_vllm_search_20260519/) contains cached GitHub bug search pages and `bug_issue_index_from_search.json`.

Use it for candidate discovery, not as final proof without reading the issue and PR evidence.

## PR-Centric Bugfix Corpus

[workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/](../../issue_capsule/workloads/pr_centric_bugfix_cases_vllm_ascend_20260601/) contains grouped PR cases, issue linkage review, changed files, patches, and commit metadata.

Key files:

- `pr_issue_correctness_review.csv`
- `pr_case_index.csv`
- `confirmed_pr_issue_links.csv`
- `prs/*/README.md`
- `prs/*/materials/code/changed_files.tsv`
- `prs/*/materials/code/patch.diff`

## Release/Image/Bugfix Mapping

[VLLM_ASCEND_RELEASE_IMAGE_BUGFIX_MAPPING_20260603.md](../../issue_capsule/project_docs/VLLM_ASCEND_RELEASE_IMAGE_BUGFIX_MAPPING_20260603.md) maps release tags, image candidates, patch bases, derived PR image names, and verification recommendations.

Supporting raw material lives in [release_image_mapping_20260603/](../../issue_capsule/project_docs/release_image_mapping_20260603/).

## Fuzzer Docs And History

[VLLM_BUG_PATTERN_TO_FUZZER_FINDABILITY.md](../../issue_capsule/project_docs/VLLM_BUG_PATTERN_TO_FUZZER_FINDABILITY.md) maps bug patterns to GRIEF-style findability classes.

[grief_fuzzer_history/](../../issue_capsule/grief_fuzzer_history/) contains smoke-run source, seeds, logs, corpus, and the run registry.

The first smoke report is [runs/2026-06-02_npu4_first_smoke/report.md](../../issue_capsule/grief_fuzzer_history/runs/2026-06-02_npu4_first_smoke/report.md).

## Environment Docs

[NPU4_ASCEND_CONTAINER_STARTUP_METHOD.md](../../issue_capsule/project_docs/NPU4_ASCEND_CONTAINER_STARTUP_METHOD.md) is the canonical npu4 container startup guide.

[ENV_CONSTRAINTS.md](../../issue_capsule/ENV_CONSTRAINTS.md) records feasible and forbidden profiles for the current npu4/v0.18.0rc1 baseline.

## CPU CI Report

Requested source: `/mnt/data/vllm_observe/vllm_ascend_cpu_ci_check/report_20260603/CPU_CI_FEASIBILITY_REPORT.md`.

Status: not found locally during this construction pass.

