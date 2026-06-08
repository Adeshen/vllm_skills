# Paper Search Workflow

## Search Sources

Use primary or near-primary sources first:

- arXiv
- ACM Digital Library
- IEEE Xplore
- USENIX
- Google Research
- OpenReview
- DBLP
- Semantic Scholar
- official project repositories
- conference pages

Use blogs, Zhihu, Papers Cool, alphaXiv, Emergent Mind, or other explainers only as supplemental intuition.

## Search Expansion

For each seed paper:

1. Exact-title search.
2. Author search for adjacent papers.
3. System-name search, such as `vLLM`, `SGLang`, `TensorRT-LLM`, `Dynamo`, `Mooncake`, `KV cache`, `prefix cache`, `diffusion serving`.
4. Method search, such as `fuzzing`, `taint analysis`, `incident taxonomy`, `continuous testing`, `disaggregated serving`, `agentic evolutionary search`.
5. Citation and reference search.
6. Artifact search for code, datasets, benchmark harnesses, or issue lists.

## Search Query Templates

```text
"<paper title>"
"<system name>" "serving" "fuzzing"
"LLM inference engine" bugs taxonomy
"LLM serving" "KV cache" "isolation"
"production incidents" "LLM inference"
"GitHub Actions" "agentic workflow injection"
"multi-architecture" "continuous testing"
"stage-level serving" diffusion pipelines
"disaggregated serving" multimodal models
"agentic evolutionary search" kernel optimization
```

## Ranking Criteria

Prioritize papers that:

- study real LLM inference/serving failures
- introduce a testing/fuzzing/evaluation method
- include artifacts, datasets, or reproducible commands
- define a useful taxonomy
- discuss production incidents or operational mitigations
- map to local bug wiki domains: scheduler, KV cache, prefix cache, streaming lifecycle, quantization, MoE, distributed/PD, metrics/tracing
- map to local feature wiki state systems

## Output Discipline

Do not return a flat list unless the user asks for one. Cluster results by research use:

- bug taxonomy
- active testing/fuzzing
- incident management
- CI and workflow security
- multi-architecture validation
- serving architecture
- kernel/operator optimization
- multimodal/diffusion serving
