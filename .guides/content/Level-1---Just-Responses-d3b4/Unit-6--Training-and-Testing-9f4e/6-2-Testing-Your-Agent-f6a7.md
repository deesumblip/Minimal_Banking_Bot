> To restart your agent, click **[Start Rasa Inspector](open_terminal panel=1. Cmd bash /home/codio/workspace/.guides/scripts/start_rasa_inspect.sh)**.
> Then click **Rasa Inspect** in the main toolbar above to load the chat tab.

#### Basic testing workflow

1. **Start Inspector** (see **Lab 6.2** if you need to run it manually).
2. **Test each flow**:
 - Type "hello" (or "hi", "hey") → should trigger the `greet` flow
 - Type "help" or "what can you do?" → should trigger the `help` flow
 - Type "contact" or "how do I reach support?" → should trigger the `contact` flow
3. **Observe**: Did the correct flow run? Did you get the expected response? Any errors?

#### Test thoroughly with variations

Test your agent with multiple phrasings so you see how the LLM matches different user messages to the same flow:

1. **Greet**: Try 3 different greetings (e.g. "hello", "hi", "good morning").
2. **Help**: Try 3 different ways to ask for help.
3. **Contact**: Try 3 different ways to ask for contact info.
4. **Goodbye**: If you added a goodbye flow, test that too.

For each test, note: what you said, which flow was activated, what the agent replied, and whether it matched your expectations. That makes it easier to spot when the wrong flow runs or a response is off.

If the wrong flow is activated, improve that flow's description (or add examples) so the command generator can match it better.
