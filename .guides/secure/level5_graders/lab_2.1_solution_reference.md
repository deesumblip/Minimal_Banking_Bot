# Lab 2.1 – Reference solution for LLM Rubric / Code Test

Use this file as the **Instructor Provided Solution File** in Codio's LLM Rubric Autograde for Lab 2.1 (Creating the Tools Folder and banking_tools.py), or as reference for the code-output-compare grader.

---

## Required structure

1. **level5/tools/** – Directory must exist.
2. **level5/tools/banking_tools.py** – Must define:
   - `check_balance(account)` (or equivalent signature)
   - `process_transfer(amount, from_account, to_account)` (or equivalent)
   - `get_account_info(account)` (or equivalent)
   - **`__all__`** – List exporting the tool function names so Rasa can discover them (e.g. `__all__ = ['check_balance', 'process_transfer', 'get_account_info']`).

Tool functions typically return a dict (e.g. `{"balance": 100}` or `{"status": "ok"}`). Docstrings help the LLM understand when to call each tool.

---

## Rubric summary for autograde

- **tools/ folder** exists under level5.
- **banking_tools.py** exists under level5/tools/.
- **Function names** check_balance, process_transfer, get_account_info appear in the file.
- **__all__** is present and exports those names (or a subset used as tools).
