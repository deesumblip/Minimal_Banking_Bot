# Lab 4.1: Understanding System Patterns

**Objective**: Explore system patterns and understand their purpose.

**Why this lab**: Before you change session start or pattern completed (Lab 4.2), you need to see where they live and how they're defined. Once you know how they trigger and what steps they run, you can safely add or change steps so the bot behaves the way you want when a conversation starts or ends.

#### Steps

1. **Open the Patterns File**
   - Navigate to `data/system/patterns/patterns.yml`
   - You should see both `pattern_session_start` and `pattern_completed`

2. **Examine `pattern_session_start`**
   - Notice it has `nlu_trigger: - intent: session_start`
   - Notice it automatically triggers; no user message is needed.
   - Notice what step it executes

3. **Examine `pattern_completed`**
   - Notice it has `noop: true` and `next: END`
   - Understand this marks the end of a conversation

**AI Coach**: Ask "When does pattern_session_start trigger?" or "What happens if I remove pattern_completed?"
