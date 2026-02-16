### 4.1 What are System Patterns?

**System patterns** are special flows that Rasa uses internally to manage conversation lifecycle. They're not user-facing flows, but rather system-level behaviors.

**File Location**: `data/system/patterns/patterns.yml`

**Analogy**: System patterns are like the operating system of your bot - they handle the "behind the scenes" stuff.

#### Two Key Patterns

1. **`pattern_session_start`**: What happens when a conversation begins
2. **`pattern_completed`**: What happens when a flow finishes

---
