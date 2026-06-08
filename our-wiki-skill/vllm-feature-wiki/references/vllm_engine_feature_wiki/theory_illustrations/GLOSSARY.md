# Glossary

This glossary is written for bug triage. It explains words in terms of state: what object exists, who mutates it, who reuses it, and how it can become inconsistent.

| Term | Mental model | State risk |
| --- | --- | --- |
| Request | One user interaction tracked by the engine from API arrival to cleanup. | Can be half-finished if scheduler, streamer, and backend disagree. |
| Sequence | Token sequence being processed for a request. | Position, mask, or block table can drift from actual tokens. |
| Prefill | The phase that processes the prompt and creates initial KV state. | Long prompt or chunked prefill can stress scheduling and cache allocation. |
| Decode | The iterative phase that emits new tokens. | Repeated steps mutate KV, output, metrics, and request status. |
| Continuous batching | The scheduler can change the active batch between decode steps. | New and old requests share resource pressure; cleanup bugs become visible. |
| KV cache | Stored key/value tensors for prior tokens. | Leaks, stale blocks, invalid transfer state, wrong reuse. |
| KV block | Fixed-size chunk of KV cache managed like a page. | Ref count/hash/ownership bugs cause false reuse or premature eviction. |
| Block table | Mapping from logical token blocks to physical KV blocks. | Wrong mapping causes attention to read wrong memory. |
| Prefix cache | Reuse of KV blocks for repeated prefixes across requests. | Hash collision, missing extra hash, stale block, wrong ref count. |
| Parent hash | Prefix context hash used to identify a block in prefix cache. | Missing parent hash breaks uniqueness and compatibility. |
| Chunked prefill | Splitting long prompt prefill into chunks. | Boundary bugs and scheduler starvation. |
| PD disaggregation | Separate prefill and decode instances connected by KV transfer. | Producer/connector/consumer can disagree about transfer success. |
| Mooncake | KV transfer/storage technology used for disaggregated serving. | Failure signals, cleanup, and metrics must be consistent. |
| Speculative decoding | Draft tokens are proposed then verified by target model. | Accepted/rejected token accounting and KV rollback can break. |
| MTP | Multi Token Prediction, a speculative-style acceleration path. | Graph/proposer state can hang or return incorrect tokens. |
| EAGLE | Speculative decoding method using a draft/proposer model. | Attention masks and repeated-call state are common risk surfaces. |
| Structured output | Grammar/schema constrained generation. | Bitmask type/shape mismatch or schema-invalid output. |
| LoRA | Adapter weights applied to a base model per request. | Adapter isolation, cache reuse, and distributed visibility risks. |
| Quantization | Reduced precision model execution. | Wrong mapping can produce garbled output with HTTP 200. |
| MoE | Mixture-of-Experts model execution. | Expert routing, FlashComm, and fused kernels are shape-sensitive. |
| Graph mode | Capturing/reusing execution graphs for performance. | Shape assumptions can fail when request shapes vary. |
| HBM | NPU high-bandwidth memory. | Multi-instance lifecycle can leak or over-allocate. |
| CPU binding | Assigning worker processes to CPU cores near devices. | Locale-dependent parser can fail before serving starts. |
| Oracle | Test rule deciding whether behavior is wrong. | Weak oracle misses correctness bugs. |
| Recovery canary | Simple request after a toxic trace. | Detects leaked scheduler/cache/backend state. |

## Fast Translation From Symptom To State

| Symptom | First state to inspect |
| --- | --- |
| HTTP 500 after KV transfer failure | connector failure state, invalid block state, metrics path |
| Hung request but service port open | scheduler progress, output handler, distributed role state |
| Wrong output with HTTP 200 | sampling, quantization, MoE, speculative acceptance |
| Good first request, bad repeated request | cached state, ref count, attention mask, adapter/proposer reuse |
| Startup before `/v1/models` fails | Ascend backend lifecycle, device mapping, CPU binding, model support |
| Metrics scrape fails after error | metrics/tracing state on failure path |

