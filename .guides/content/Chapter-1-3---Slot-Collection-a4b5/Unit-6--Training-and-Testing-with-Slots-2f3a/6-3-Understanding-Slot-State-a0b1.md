# 6.3 Understanding Slot State

In Inspector you can see slot values in the debug panel. Before collection you might see `account: null`. After the user provides a value you'll see `account: "1234"`. The action can read that same value when it runs.

Slots persist throughout the conversation until the session ends.
