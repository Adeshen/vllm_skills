# vLLM Feature Wiki Examples

## Example 1: "Improve KV cache theory"

1. Open `kv_cache/README.md`, `prefix_cache/README.md`, and `theory_illustrations/KV_CACHE_DEEP_DIVE.md`.
2. Open bug capsules linked from those pages.
3. Add a clearer state story for block table, block hash, ref count, eviction, and transfer invalidation.
4. Update `feature_to_bug_map/README.md` if new bug links are added.
5. Run `scripts/validate_wiki.py`.

## Example 2: "Add official Ascend feature coverage"

1. Browse official vLLM-Ascend feature docs.
2. Update `OFFICIAL_FEATURE_COVERAGE.md` with source links and coverage status.
3. Add only evidence-supported details to subsystem pages.
4. Mark unsupported or unverified behavior `unknown`.

## Example 3: "Connect a new bug to feature state"

1. Open the bug capsule.
2. Identify the failing state object: scheduler request, KV block, attention mask, sampler bitmask, connector transfer, HBM allocation.
3. Update the relevant subsystem page under `Related Bugs` and `Common Bug Stories`.
4. Update `feature_to_bug_map/README.md`.
5. Add fuzzer implications only if the workload can be expressed as request traces or monitored externally.

## Example 4: "Create a new feature page"

1. Create `new_feature/README.md` using `FEATURE_TEMPLATE.md`.
2. Add a row to `INDEX.md`.
3. Add source links and unknowns.
4. Add map rows only for existing bug evidence.
5. Validate structure.

## Example 5: "Connect a feature to official vLLM skills"

1. Open `references/vllm_skills.md`.
2. Identify whether the feature needs deploy, endpoint benchmark, synthetic benchmark, or prefix-cache benchmark support.
3. Update the feature page's `Verification Strategy` with the skill route, not a fabricated command.
4. Keep Ascend-specific differences explicit: official vLLM skills are generic unless local evidence proves Ascend adaptation.
5. Validate.
