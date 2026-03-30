**Starting point:** Work in **`level5/`** with **Lab 2.0** complete (**`data/prompts/command_prompt_v3_slot_names.jinja2`** and **`prompt_template`** in **`config.yml`**) and the Chapter 1.4 completion baseline otherwise unchanged.

In this lab you complete **`banking_tools.py`** in the fill-in-the-blanks exercise, then create **`level5/tools/`** and save the same module as **`level5/tools/banking_tools.py`**. The module must define **`check_balance`**, **`process_transfer`**, and **`get_account_info`**, export them in **`__all__`**, and use the patterns from **Unit 2.1** (type hints, docstrings, return dicts).

You do **not** need to activate the virtual environment for this lab; **Check It!** only checks your saved files on disk.

---

#### Complete the `banking_tools` module (fill in the blanks)

The exercise uses the same ideas as **Unit 2.1**: **`str`** type hints on **`account`**, docstrings that tell the LLM **when** to call each tool, and **return dict keys** like the **`check_balance`** example on the previous page. The **`__all__`** line is **shown in full** (no blanks there). **Twelve blanks** cover **`str`** (for **`check_balance`** and **`get_account_info`**), the three docstrings, and the keys **`balance`**, **`currency`**, **`status`** (first **`return`**), **`success`**, **`message`**, **`account_type`**, and **`status`** (second **`return`**). Demo numbers and strings in the return dicts are **not** blanked. Complete every blank, then **copy the full script** into **`level5/tools/banking_tools.py`**. Run the **Code Test** when the file is saved.

{Check It!|assessment}(fill-in-the-blanks-501020010)

---

### After you complete the blanks

1. In **`level5/`**, create a directory named **`tools`** (if it does not exist).
2. Create **`level5/tools/__init__.py`** (can be empty or a short comment).
3. **Open** **`level5/tools/banking_tools.py`** in the file tree (create the file if needed).
4. **Paste** your completed script from the exercise above so the file matches your answers (all blanks filled).
5. **Save** the file.

---

### Run the code assessment

The grader checks that **`level5/tools/`** exists, **`banking_tools.py`** is present, **`check_balance`**, **`process_transfer`**, and **`get_account_info`** appear in the file, and **`__all__`** is defined.

{Check It!|assessment}(code-output-compare-501020001)

---

**Success criteria.** Code test passes (**10/10**). Then continue to **Lab 3.1**.

---

## Running locally

1. `cd level5`.
2. Complete the **fill-in-the-blanks** exercise, then create **`tools/`**, **`tools/__init__.py`**, and **`tools/banking_tools.py`** with the completed script.
3. Run the **Code Test** when your files match the exercise.
