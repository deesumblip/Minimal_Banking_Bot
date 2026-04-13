To let users "talk to the banking assistant," you need a **flow** that the main agent can run and whose steps include **calling** the sub-agent. The flow does not implement the sub-agent’s behaviour. It has a step that hands off to the sub-agent by name.

## Shape of the flow (Lab 4.1)

You **create** **`level6/data/basics/ask_banking_assistant.yml`** in the lab. It is not shipped as a complete file in the starter repo. The file should define a flow (under the top-level **`flows:`** key) with:

- A **flow id** (e.g. `ask_banking_assistant`) and human-readable **`name`** / **`description`** so SearchReady can choose when the user wants the **specialist** (not a generic balance check).
- **`steps`** that include at least:
 - **`call: banking_assistant`**, must match **`agent.name`** in **`sub_agents/banking_assistant/config.yml`**.
 - Optionally a follow-up such as **`action: utter_help`** so the main agent can offer help again after the sub-agent finishes.

Illustrative shape under **`flows:`** (you set **`name`** / **`description`** yourself in Lab 4.1):

```yaml
flows:
  ask_banking_assistant:
    name: "Human-readable title for SearchReady"
    description: "When the user wants the banking specialist…"
    steps:
      - call: banking_assistant
      - action: utter_help
```

Write **`name`** and **`description`** yourself so they fit your course wording. Do not rely on a single canned paragraph from the guide.

In **Lab 4.1** you complete a **Fill in the blanks** for the full flow file (including **`flows:`**), **save** it as **`ask_banking_assistant.yml`**, then run **Check It!**, same **fill-in → copy → code test** pattern as **Level 5 Lab 4.1** (domain slot conditions + flow).
