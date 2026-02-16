#### Basic Testing Workflow

1. **Start Inspector** (see 6.3).
2. **Test each flow**:
   - Type "hello" → Should trigger `greet` flow
   - Type "help" → Should trigger `help` flow
   - Type "contact" → Should trigger `contact` flow
3. **Observe**: Correct flow? Expected response? Any errors?

#### Understanding Flow Triggers

The LLM uses flow descriptions to match user messages. For example:
- **Flow**: `greet` with description "Greet the user when they start a conversation"
- **User says**: "hello", "hi", "hey", "good morning"
- **Result**: All trigger the `greet` flow because the LLM understands they're greetings
