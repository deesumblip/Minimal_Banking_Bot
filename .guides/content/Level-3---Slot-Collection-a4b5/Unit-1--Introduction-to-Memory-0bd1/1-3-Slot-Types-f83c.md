The slot type controls what kind of value the slot accepts. Use the type that matches the shape of the data you are storing.

| Type | Stores | Example values |
|---|---|---|
| `text` | Any string | `"1234"`, `"John Doe"`, `"checking"` |
| `bool` | True or false | `true`, `false` |
| `float` | Decimal number | `99.95`, `0.5` |
| `categorical` | One value from a predefined set | `"low"`, `"medium"`, `"high"` |
| `any` | Anything, including dicts | `{"balance": 123.45, "currency": "USD"}` |

Level 3 uses `text`. Other types appear in later levels.

**Naming.** Use lowercase descriptive names with underscores for multi-word slots. `account`, `user_name`, and `transfer_amount` are clear. `a`, `slot1`, and `data` are not.