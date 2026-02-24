Your goal is to **complete** the action file that reads the `account` slot and handles placeholder values. The domain already lists `action_check_balance_simple` from Lab 3.1; here you fill in the blanks so the Python file is correct.

---

## Fill-in-the-blanks exercise

1. **Create** the file `level3/actions/action_check_balance_simple.py` in your project.

2. **Copy the script template** (see Lab 4.1 assessment notes) into that file. The script has **eleven blanks** marked `(1)` through `(11)` **in order** as you read from top to bottom.

3. **Replace each blank** with the correct code. Each blank is a single expression or value (one line). The blanks reinforce concepts from Level 1 (domain, responses), Level 2 (actions, `run`/`name`, dispatcher), and Level 3 (slots, placeholders).

4. **Save** the file, then **run the assessment**. The grader checks that the file exists, has the right structure, reads the slot, handles placeholders, and sends the balance message.

---

### After you finish

- **Verify** your domain (from Lab 3.1) lists `action_check_balance_simple` in the `actions:` section.
- **Run the assessment** when you're done.
- **Optional.** After Lab 6.1, train and run Inspector. Trigger the check_balance flow and watch the action use the slot and re-ask when the LLM extracts a placeholder.
