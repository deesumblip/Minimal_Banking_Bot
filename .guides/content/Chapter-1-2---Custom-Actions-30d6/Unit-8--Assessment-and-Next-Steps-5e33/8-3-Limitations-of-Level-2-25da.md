Level 2 bots have clear limitations:

#### What Level 2 Cannot Do

1. **Remember Information**: The bot cannot remember what the user said earlier
   - Example: User says "My account is 1234" → Bot forgets immediately
   - Solution: Level 3 adds slots (memory)

2. **Use Previous Context**: Actions can't access conversation history effectively
   - Example: "Check my balance" → Bot doesn't know which account
   - Solution: Level 3 adds slots to remember account numbers

3. **Collect Multiple Pieces of Information**: Can't gather multiple data points
   - Example: "Transfer money" → Bot can't collect amount, recipient, and account
   - Solution: Level 4 adds multiple slot collection

#### When Level 2 is Sufficient

Level 2 is perfect for:
- Dynamic responses based on calculations
- Data processing and formatting
- Simple integrations (APIs, databases)
- Conditional logic that doesn't need memory

#### When You Need More

Move to Level 3 when you need:
- Memory (slots) to remember user information
- Multi-turn conversations with context
- Collecting information from users

---
