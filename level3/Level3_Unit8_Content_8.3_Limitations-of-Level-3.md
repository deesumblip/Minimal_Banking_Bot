# 8.3 Limitations of Level 3

## What Level 3 Cannot Do

1. **Collect Multiple Slots Efficiently**: Can only collect one slot at a time easily
   - Example: "Transfer money" needs amount, recipient, and account
   - Solution: Level 4 adds multiple slot collection

2. **Complex Validation**: Limited validation of slot values
   - Example: Can't easily validate account format
   - Solution: Can be handled in actions, but Level 4 makes it easier

## When Level 3 is Sufficient

Level 3 is perfect for:
- Single piece of information (account number, name)
- Simple multi-turn conversations
- Remembering one key piece of data

## When You Need More

Move to Level 4 when you need:
- To collect multiple pieces of information
- Complex forms with multiple fields
- Validating multiple slot values together
