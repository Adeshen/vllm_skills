# vLLM Ascend Incident Workflow

Use this compact sequence during incident handling:

1. Read-only baseline bundle first.
2. Preserve trigger request or request mix.
3. Replay on a clean target.
4. Collect replay-time bundle.
5. Branch into:
   - trace for slow-path ambiguity
   - repro for issue-shaped crashes
   - hang-time stacks or watchdog evidence for stalls
6. Normalize the report.

The point is to avoid losing the original scene before the replay path is ready.
