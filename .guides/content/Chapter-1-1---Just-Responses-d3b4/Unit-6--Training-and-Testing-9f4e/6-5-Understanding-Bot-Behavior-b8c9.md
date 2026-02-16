### 6.5 Understanding Bot Behavior

#### How the Bot Decides What to Do

1. User sends a message (e.g. "hello").
2. Pipeline (LLM) processes the message and understands intent.
3. FlowPolicy searches flows and matches the best flow description.
4. Rasa runs that flow's steps (e.g. `utter_greet`).
5. Domain provides the response text; the bot replies.

Training builds a model that encodes your flows and domain so this process runs correctly at runtime.
