# 8.4 What's Next: Level 4 Preview

**Important. Building on Your Existing Banking Bot**

When you move to Level 4, you will continue working on the same banking bot you've built throughout Levels 1, 2, and 3. Level 4 doesn't start from scratch. It builds on what you've already created.

Your existing responses (all Level 1–3 responses) stay. Your existing flows (all Level 1–3 flows) stay. Your existing actions (all Level 2–3 actions) stay. Your existing slots (`account`) stay. Level 4 adds more slots, more ask responses, actions that use multiple slots, and flows that collect multiple slots.

You don't start a new bot. You extend your existing Level 3 banking bot with multiple slot collection.

---

**Level 4: Multiple Slots** introduces collecting multiple pieces of information.

## What Multiple Slots Enable

**Example scenario.** "Transfer $100 to John from account 1234"

Level 3 can only easily collect one piece of information at a time. Level 4 can collect amount ($100), recipient (John), and source account (1234), all in one flow, in order.

In Level 4 you'll add additional slots (`amount`, `recipient`, `account_from`), additional ask responses (`utter_ask_amount`, `utter_ask_recipient`, `utter_ask_account_from`), an `action_process_transfer` action that uses all three slots, and a `transfer_money` flow that collects all three slots before processing.

## Key Concepts in Level 4

1. **Multiple Slot Collection.** Collecting several slots in sequence.
2. **Slot Validation.** Ensuring all required slots have valid values.
3. **Complex Conversations.** Handling users who provide information in different orders.

## When to Move to Level 4

Move to Level 4 when you need to collect multiple pieces of information before performing an action, handle complex forms or multi-step data collection, or build actions that require multiple data points.

Your Level 3 banking bot is the foundation. Level 4 adds multiple slot collection on top of it.
