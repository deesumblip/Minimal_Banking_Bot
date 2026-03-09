### 4.3 Pattern Completed

The `pattern_completed` flow handles what happens when a flow finishes.

**Why it matters**: After the bot has answered, for example with hours or contact info, the conversation needs a clear "we're done with this turn." Pattern completed tells Rasa to end the flow and wait for the next user message. Without it, the bot might not cleanly transition back to listening.

```yaml
flows:
  pattern_completed:
    description: A flow has been completed and there is nothing else to be done
    steps:
      - noop: true
        next: END
```

- **`pattern_completed`**: Special name; triggers when a flow completes.
- **`noop: true`**: No operation – placeholder step.
- **`next: END`**: Tells Rasa the conversation is complete; bot waits for next user message.

---
