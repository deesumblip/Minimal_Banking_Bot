# 6.3 Understanding Slot State

In Inspector, you can see slot values in the debug panel:
- **Before collection**: `account: null`
- **After user provides**: `account: "1234"`
- **In action**: Action can read `account: "1234"`

**Key point**: Slots persist throughout the conversation until the session ends.
