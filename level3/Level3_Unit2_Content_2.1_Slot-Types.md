# 2.1 Slot Types

Slots can have different types. For Level 3, we use the simplest type: `text`.

## Text Slots

```yaml
slots:
  account:
    type: text
```

**Text slots**:
- Store any text value
- Most flexible type
- Good for: names, account numbers, descriptions, any text input

**Example values**:
- `"1234"` (account number)
- `"John Doe"` (name)
- `"checking"` (account type)

## Other Slot Types (Advanced)

For Level 3 we only use `text` slots. Other types exist (e.g. `bool`, `float`, `list`) but are covered in advanced tutorials.
