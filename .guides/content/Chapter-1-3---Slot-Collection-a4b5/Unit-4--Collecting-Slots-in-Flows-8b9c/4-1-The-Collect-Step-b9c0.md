The `collect:` step in a flow tells Rasa: "Get this slot value before continuing."

## Collect Step Structure

```yaml
steps:
  - collect: account
    description: "account number"
```

- **`collect: account`** — Which slot to collect
- **`description:`** — Helps the LLM understand what to extract (optional but recommended)
