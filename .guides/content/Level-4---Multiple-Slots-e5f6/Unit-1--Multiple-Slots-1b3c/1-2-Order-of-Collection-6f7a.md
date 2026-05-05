The order of `collect:` steps in the flow is the order the agent asks for values when slots are empty.
 
```yaml
steps:
  - collect: account
  - collect: amount
  - collect: recipient
  - action: action_process_transfer
```
 
Rasa walks the list top to bottom. If a slot already has a value when its step is reached, that step is skipped. The action runs only after all collected slots have values.
 
Because `account` is collected first, a user who already provided their account number during a balance check in the same session will not be asked again. The flow moves straight to `amount`.
 