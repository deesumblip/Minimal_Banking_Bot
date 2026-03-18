**YAML** (Yet Another Markup Language) is a human-readable format for configuration files. Rasa uses YAML extensively, so understanding the basics is essential.

#### Why YAML?

YAML is designed to be easy for humans to read and write, making it perfect for configuration files. All Rasa bot files use YAML format.

#### Basic YAML Rules

1. **Indentation Matters**
   - Use **2 spaces** (not tabs, not 4 spaces)
   - Indentation shows hierarchy (what belongs to what)
   - Incorrect indentation will cause errors

2. **Key-Value Pairs**
   ```yaml
   key: value
   name: "Hello World"
   number: 42
   ```

3. **Lists (Arrays)**
   ```yaml
   # List of items (each item starts with a dash and space)
   items:
     - item1
     - item2
     - item3
   ```

4. **Colons and Dashes**
   - **Colon (`:`)** separates keys from values: `key: value`
   - **Dash (`-`)** indicates a list item: `- item`
   - Always put a space after colons and dashes

5. **Quotes**
   - Use quotes around text with special characters
   - Simple strings don't need quotes: `name: Hello`
   - But it's safer to use quotes: `name: "Hello World"`

#### YAML Examples

**CORRECT Examples:**

```yaml
# Simple key-value pair
version: "3.1"

# List of items (notice the 2-space indentation)
responses:
  utter_greet:
    - text: "Hello!"        # ← 4 spaces before '-', 6 before 'text:'
      metadata:              # ← 6 spaces (same level as 'text:')
        rephrase: True       # ← 8 spaces (under 'metadata:')
```

**WRONG Examples:**

```yaml
# ❌ WRONG: Missing space after colon
version:"3.1"

# ❌ WRONG: Using tabs instead of spaces
responses:
	utter_greet:
		- text: "Hello!"

# ❌ WRONG: Wrong indentation (using 4 spaces instead of 2)
responses:
    utter_greet:
        - text: "Hello!"

# ❌ WRONG: Missing dash for list item
responses:
  utter_greet:
    text: "Hello!"  # ← Should be: - text: "Hello!"
```

#### YAML Quick Reference

| Element | Syntax | Example |
|---------|--------|---------|
| Key-value | `key: value` | `name: "Hello"` |
| List item | `- item` | `- "First item"` |
| Nested structure | Indent 2 spaces | `parent:`<br>`  child: value` |
| Comments | `# comment` | `# This is a comment` |

⚠️ **Common YAML Mistakes**:
1. Using tabs instead of spaces
2. Wrong indentation (not using 2 spaces consistently)
3. Missing colons after keys
4. Missing dashes before list items
5. Mixing 2-space and 4-space indentation

**Tip**: Most modern text editors (VS Code, PyCharm) can validate YAML syntax and highlight errors.

{Check It!|assessment}(multiple-choice-2974857363)