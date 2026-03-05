### 7.3 Best Practices

#### Organizing Actions

1. **One action per file**: Makes it easier to find and modify actions
2. **Descriptive names**: Use clear, descriptive action names
3. **Group related actions**: Keep related actions in the same folder

#### Writing Good Actions

1. **Keep actions focused**: Each action should do one thing well
2. **Handle errors gracefully**: Check for None values, validate input
3. **Use clear messages**: Make sure users understand what happened
4. **Add comments**: Explain complex logic

#### Action Naming Conventions

- **Good**: `action_bank_hours`, `action_check_balance`, `action_process_transfer`
- ❌ **Bad**: `action1`, `hours`, `do_stuff`

**Convention**: `action_` + descriptive_name (lowercase, underscores)

---
