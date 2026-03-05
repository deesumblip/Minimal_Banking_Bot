### 4.3 Pattern Completed

The `pattern_completed` flow handles what happens when a flow finishes.

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
