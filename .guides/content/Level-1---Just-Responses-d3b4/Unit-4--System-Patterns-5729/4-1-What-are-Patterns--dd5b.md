
**Patterns** are special system flows that Rasa uses internally to manage conversation lifecycle. They're not user-facing flows, but rather system-level behaviors.

**File Location**: `data/system/patterns/patterns.yml`

**Analogy**: System patterns are like the operating system of your agent, they handle the "behind the scenes" stuff.

#### Two Key Patterns We Will Learn

1. **`pattern_session_start`**: What happens when a conversation begins
2. **`pattern_completed`**: What happens when a flow finishes

---

#### Bonus

You don't need to know all of these now, but if you want to get a sense of all the different patterns Rasa offers, you can see them below and read about them in the [documentation](https://rasa.com/docs/reference/primitives/patterns/). 
| Pattern | Triggered when |
|---|---|
| `pattern_session_start` | A conversation begins |
| `pattern_completed` | A flow finishes successfully |
| `pattern_cancelled` | A user abandons a flow mid-way |
| `pattern_clarification` | The command generator is not confident which flow to start |
| `pattern_correction` | A user corrects something they said earlier |
| `pattern_cannot_handle` | No flow matches the user's request |
| `pattern_internal_error` | A system error occurs at runtime |
| `pattern_chitchat` | A user sends an off-topic or casual message |
| `pattern_repeat_bot_messages` | A user asks the agent to repeat the last message |
| `pattern_customer_satisfaction` | A conversation ends, triggering a CSAT message |

All patterns follow the same YAML structure as any other flow. Your business flows stay focused on the task. Patterns handle everything else.