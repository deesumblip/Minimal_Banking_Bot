### 1.2 The Simplest Agent Possible

Level 1 represents the **absolute minimum** a functional Rasa agent needs. We intentionally start simple to build a solid foundation.

#### What Level 1 Includes

- **Responses**: Predefined messages the agent can say
- **Flows**: Simple conversation scripts that use those responses
- **Basic configuration**: Files that tell Rasa how to build the agent

#### What Level 1 Does NOT Include

- **Slots (Memory)**: The agent cannot remember information from earlier in the conversation
- **Actions (Custom Code)**: The agent cannot execute Python code or perform calculations
- **Dynamic Responses**: All responses are static - they don't change based on context

#### Why Start Here?

1. **Minimal Cognitive Load**: You only need to understand one concept: responses
2. **Quick Wins**: You can build a working agent in minutes
3. **Real-World Validity**: Many production agents are exactly this simple
4. **Foundation**: Everything else builds on this base

**Analogy**: Level 1 is like a FAQ page that can understand questions. It provides information, but doesn't do anything complex.

---
