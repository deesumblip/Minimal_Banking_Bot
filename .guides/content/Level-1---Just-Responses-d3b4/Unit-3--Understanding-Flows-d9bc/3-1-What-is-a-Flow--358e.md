A **flow** is a conversational path the agent runs from start to finish. It encodes the business logic for a single process: an ordered plan for what to do when that process applies.
 
Flows sit at the guided end of the autonomy spectrum. Use them when the steps are known in advance, order matters, and the language model should not invent the sequence.
 
**Flow structure**
 
```yaml
flows:
  greet:                        # Flow ID — unique, lowercase
    name: say hello             # Optional human-readable label
    description: Greet the user when they start a conversation
    steps:
      - action: utter_greet     # Calls the response from domain/basics.yml
```
 
The Command Generator reads `description:` (and `name:` if present, otherwise the flow ID) to decide which flow to activate. A vague or missing description means the flow won't activate reliably.
 
<table style="width:100%;border-collapse:collapse;margin:16px 0;"><tr style="background:transparent;border:none;"><td style="background:#ebe8fe;border:1px solid #c4baf9;border-left:3px solid #5a17ee;padding:12px 16px;line-height:1.6;color:#080327;font-size:0.9em;"><strong><code>description:</code> is the most important field in a flow.</strong> The LLM reads it to decide when to activate the flow. Everything else can be correct and it will be hard to get the flow to activate at the right times if the description is vague or missing.</td></tr></table>

**Flows live in** `data/basics/*.yml`. One file per flow, or several related flows in the same file.
 
**Execution**
 
```text
User says "hello"
  ↓
Flow greet activates
  ↓
Step 1: utter_greet
  ↓
Agent responds: "Hi! I'm a banking assistant..."
  ↓
Flow completes
```
 
---