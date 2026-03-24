### 3.3 Flow Descriptions and LLM Understanding

The `description` field is **critical** because the LLM uses it to match user messages to flows.

**Why descriptions matter**: Users don't type keywords. They say things like "when are you open?" or "what's your phone number?" The LLM has to decide which flow fits. Your description is the only place you tell it "this flow is for bank hours" or "this flow is for contact info." A clear description means the right flow runs; a vague one means the agent might pick the wrong flow or none at all.

#### How It Works

1. User sends a message: "I need help"
2. LLM reads all flow descriptions
3. LLM matches the message to the best-fitting description
4. Rasa triggers that flow

#### Writing Good Descriptions

✅ **Good descriptions**:
- Clear and specific: "Greet the user when they start a conversation"
- Action-oriented: "Provide contact information for the bank"
- Context-aware: "Explain what the agent can help with"

❌ **Bad descriptions**:
- Too vague: "Help user" (what kind of help?)
- Too specific: "Respond when user says exactly 'hello'" (misses "hi", "hey")
- Missing context: "Say hello" (when? why?)

#### Example: Matching Process

**Flow Description**: "Greet the user when they start a conversation"

**User Messages That Match**: "hello", "hi", "hey there", "good morning", "greetings"

**Why**: The LLM understands all these are greetings that start conversations.

**Next:** In **Lab 3.4**, complete the hours and balance flow YAML with fill-in-the-blank practice, then **Lab 3.5** adds those flows and responses to your project.

---
