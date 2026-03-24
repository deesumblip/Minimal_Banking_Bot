Slots follow the same story each time. You define them in the domain, you collect them in a flow, and you read them in an action when you need the value.

**Step 1. Define the slot** in `domain/basics.yml`:


slots:
  account:
    type: text

**Step 2. Collect the slot** in a flow:


steps:
  - collect: account
    description: "account number"

**Step 3. Read the slot** in an action:


account = tracker.get_slot("account")

These three steps are the core of slot-based memory in Level 3. You will walk through them in order in the labs in this chapter.
