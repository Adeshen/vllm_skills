---
name: paper-skill
description: Search, triage, and synthesize related papers for vLLM, LLM inference engines, LLM serving fuzzing, MLSys, incident management, CI/security, and agentic research workflows. Use when the user asks to find related papers, expand a reading list, build a paper map, compare papers, extract research gaps, connect literature to bug/feature wiki topics, or seed a literature review from known paper titles.
---

# Paper Skill

Use this skill to turn a known paper list into a living literature map. It is optimized for LLM serving, inference-engine bugs, fuzzing, production incidents, multi-architecture CI, workflow security, disaggregated serving, multimodal/diffusion serving, and agentic optimization.

## Golden Rules

- **Primary source first.** Prefer arXiv, venue pages, publisher pages, official project repositories, DBLP, Semantic Scholar, or Google Research pages.
- **Search graph, not one query.** Expand by title, authors, citations, references, venue, keywords, and systems named in the paper.
- **Separate paper claims from local evidence.** A paper can motivate a bug/wiki direction but does not prove a local vLLM or vLLM-Ascend fact.
- **Preserve uncertainty.** If venue, version, artifact, or relationship is unknown, write `unknown`.
- **Connect to action.** Every paper cluster should end with what it suggests for bug capsules, feature pages, fuzzer seeds, incident SOPs, or CI tests.

## Core Workflow

1. Read [references/seed_papers.md](references/seed_papers.md) for the known reading set.
2. Read [references/search_workflow.md](references/search_workflow.md) before searching.
3. Read [references/topic_taxonomy.md](references/topic_taxonomy.md) to classify papers by local wiki relevance.
4. Search primary sources first. If the user asks for current/latest papers, browse and cite sources.
5. Build a paper map table:
   - title
   - year/date
   - source URL
   - topic cluster
   - key idea
   - local relevance
   - evidence status
   - next local action
6. For each promising paper, add relation edges:
   - cites / cited by
   - same authors/lab
   - same system
   - same failure domain
   - same testing method
   - same deployment problem
7. Return the smallest useful synthesis, not a raw search dump.

## Local Output Shapes

For a quick search request, return:

```text
cluster -> papers -> why relevant -> local action
```

For a literature review request, create or update a Markdown artifact with:

```text
# Paper Map: <topic>

## Seed Papers
## Related Papers Found
## Topic Clusters
## Method Comparison
## Local Wiki Connections
## Open Research Gaps
## Next Search Queries
```

## Local Connections

- Bug wiki: use papers to refine bug taxonomy, failure domains, reproduction evidence expectations, and fuzzer discoverability language.
- Feature wiki: use papers to improve state-machine theory and serving architecture explanations.
- Operator skills: use incident, tracing, benchmark, and CI papers to sharpen runbooks and validation contracts.
- Fuzzer work: use fuzzing papers to define seed shape, mutation axes, oracle design, replay, and triage policy.

## Tools And Scripts

- Use [scripts/make_queries.py](scripts/make_queries.py) to generate search queries from the seed paper list.
- Use [references/seed_papers.md](references/seed_papers.md) as the current known reading set.

## Validation

A paper-search result is valid only when it cites primary sources for paper identity, separates confirmed facts from inferred relevance, groups papers by topic, and ends with concrete local next actions.
