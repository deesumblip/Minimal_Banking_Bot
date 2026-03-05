### 3.3 Flow Descriptions and LLM Understanding

The `description` field is **critical** because the LLM uses it to match user messages to flows.

#### How It Works

1. User sends a message: "I need help"
2. LLM reads all flow descriptions
3. LLM matches the message to the best-fitting description
4. Rasa triggers that flow

#### Writing Good Descriptions

✅ **Good descriptions**:
- Clear and specific: "Greet the user when they start a conversation"
- Action-oriented: "Provide contact information for the bank"
- Context-aware: "Explain what the bot can help with"

❌ **Bad descriptions**:
- Too vague: "Help user" (what kind of help?)
- Too specific: "Respond when user says exactly 'hello'" (misses "hi", "hey")
- Missing context: "Say hello" (when? why?)

#### Example: Matching Process

**Flow Description**: "Greet the user when they start a conversation"

**User Messages That Match**: "hello", "hi", "hey there", "good morning", "greetings"

**Why**: The LLM understands all these are greetings that start conversations.

---
