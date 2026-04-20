The `config.yml` file tells Rasa **how to build your agent**. It's like the blueprint that defines the agent's architecture.

**File Location**: `config.yml` (root of your agent folder)

#### Complete config.yml Breakdown

```yaml
recipe: default.v1
language: en
assistant_id: level1-agent

pipeline:
  - name: SearchReadyLLMCommandGenerator
    llm:
      model_group: rasa_command_generation_model
    flow_retrieval:
      active: false

policies:
  - name: FlowPolicy
```

#### Section-by-Section Explanation

| Field | What it does |
|---|---|
| `recipe` | Sets the base configuration template. `default.v1` is standard for all Rasa projects. |
| `language` | Sets the agent's language. `en` for English, `fr` for French, and so on. |
| `assistant_id` | A unique name for this agent, it is visible in logs and tracking so you can compare different versions. |
| `pipeline` | Defines how Rasa understands user messages. `SearchReadyLLMCommandGenerator` is the command generator selected for this agent. It reads each flow's `description:` and decides which flow to start. |
| `model_group` | References the LLM configuration defined in `endpoints.yml`. Rather than adding a model in `config.yml`, Rasa uses model groups to keep model definitions separate from pipeline configuration. You can swap the underlying LLM in `endpoints.yml` without touching `config.yml`. |
| `flow_retrieval` | When an agent has many flows, sending every flow description to the LLM on every turn is slow and expensive. You can use Flow retrieval to pre-select only the flows relevant to the current message. Set to `false` here because this project has only a few flows. |
| `policies` | Defines how Rasa decides what to do next. `FlowPolicy` is the chosen policy for this project. |



{Check It!|assessment}(multiple-choice-2496482437)

---
