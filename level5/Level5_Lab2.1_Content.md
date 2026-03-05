**Objective.** In this lab you will create the `tools/` folder and `tools/banking_tools.py` with at least three tool functions that the LLM can call: `check_balance(account)`, `process_transfer(amount, from_account, to_account)`, and `get_account_info(account)`.

## Step-by-Step Instructions

**Step 1.** In the `level5` folder, create a directory named `tools` (if it does not exist).

**Step 2.** Create `tools/__init__.py` (can be empty or a short comment that this is the tools module).

**Step 3.** Create `tools/banking_tools.py`. Define three functions:

- **check_balance(account: str)** — Returns a dict (e.g. with keys such as `account`, `balance`, `currency`). Include a docstring describing that it checks the balance for a bank account.
- **process_transfer(amount: str, from_account: str, to_account: str)** — Returns a dict (e.g. `success`, `message`). Docstring: process a money transfer from one account to another.
- **get_account_info(account: str)** — Returns a dict (e.g. account type, status). Docstring: get information for a bank account.

**Step 4.** At the top of `banking_tools.py`, add: `__all__ = ["check_balance", "process_transfer", "get_account_info"]` so Rasa can discover these tools.

**Step 5.** Verify: the `tools/` folder exists, `banking_tools.py` has the three functions with docstrings and type hints, and `__all__` lists them.

---

## In Codio

1. From project root run `source .venv/bin/activate`, then `cd level5`.
2. Create `level5/tools/` and `level5/tools/__init__.py`, then `level5/tools/banking_tools.py` with the three functions and `__all__`.
3. Run the assessment when done.

{Check It!|assessment}(code-output-compare-501020001)

## Running locally

1. Open the project, activate the venv, `cd level5`.
2. Create the `tools` folder and files as above. Run the assessment when done.
