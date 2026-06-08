# Lifecycle / Cancel

## Common Failure Symptoms
- Streaming client disconnect leaves request state behind.
- Cancelled request kills or stalls output handler.
- Recovery request fails after disconnect.
- Engine remains listening but no longer progresses.

## Issue/PR Examples
- No initial capsule is a pure cancel/disconnect bug.
- The GRIEF smoke report includes a streaming seed, and the fuzzer findability doc identifies cancel/disconnect lifecycle bugs as directly findable when a target issue is available.
- PD proxy and hang cases in the PR-centric corpus are good future candidates after source review.

## Workload Trigger Axes
- Streaming enabled.
- Client disconnect timing.
- Cancel request after first token or before first token.
- Retry storm after cancel.
- Recovery canary after cleanup.

## Useful Fuzzer Seed Shapes
- Streaming request -> disconnect -> immediate canary.
- Long-running request -> cancel -> retry same prompt.
- Burst of short streams with randomized disconnect timing.

## Useful Oracle/Monitor Design
- No tokens after cancel.
- No 5xx from output handler.
- Recovery canary must complete.
- Queue/request count returns to baseline.

## Evidence Still Missing
- vLLM-Ascend-specific cancel/disconnect issue capsule.
- Cancel/disconnect support in the current GRIEF run harness on npu4.
- Request-state metrics exposed from the service.

