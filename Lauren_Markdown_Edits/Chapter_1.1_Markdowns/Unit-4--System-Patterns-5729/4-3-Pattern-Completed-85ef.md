The `pattern_completed` flow handles what happens when a flow finishes.

```yaml
flows:
  pattern_completed:
    description: A flow has been completed and there is nothing else to be done
    steps:
      - noop: true
        next: END
```

#### Breaking It Down

1. **`pattern_completed`**: Special name Rasa recognizes
   - Must be exactly this name
   - Triggers when a flow completes

2. **`- noop: true`**: No operation
   - `noop` means "no operation" - do nothing
   - Just a placeholder step

3. **`next: END`**: End the conversation
   - Tells Rasa the conversation is complete
   - Bot waits for next user message

#### When It Triggers

After any flow completes, if there's nothing else to do, `pattern_completed` runs and the conversation ends (waits for next input).

---