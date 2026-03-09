# Lab 7.1: Complete Bot Walkthrough

**Objective**: Understand how all pieces work together in a complete conversation.

**Why this lab**: You've built each piece (session start, flows, domain) in isolation. Here you run one full conversation and watch which pattern and flows trigger at each step. That reinforces how the bot decides what to do and makes it easier to fix issues when a flow doesn't run or the wrong one runs.

#### Steps

1. **Start Inspector** if not already running.
2. **Have a complete conversation**: Open a new session so that `pattern_session_start` runs. Ask for help, ask for contact info, then end the conversation.
3. **Observe**: Which flow triggers for each message; use debug output to see LLM understanding; see how flows and responses connect.

**AI Coach**: Ask "How does the bot decide which flow to trigger?" or "What happens when I start a new conversation?"
