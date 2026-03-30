**Starting point:** Work in **`level5/`** with **Lab 2.1** complete (**`tools/banking_tools.py`** and **`__all__`**).

**Objective.** The **previous page** showed the **`tools:`** section in **`endpoints.yml`**. In this lab you add it to **`level5/endpoints.yml`** so Rasa can discover the tool functions you created in the **previous unit’s lab**.

## Step-by-Step Instructions

**Step 1.** Confirm **`level5/tools/__init__.py`** exists (Lab 2.1). Rasa loads **`tools`** as a Python package; without **`__init__.py`**, registration can fail.

**Step 2.** Open `level5/endpoints.yml`. Ensure existing sections (action_endpoint, nlg, model_groups) are unchanged.

**Step 3.** Add a new section **tools** (e.g. after the action_endpoint or before model_groups):

```yaml
tools:
  tools_module: "tools"
```

Use 2-space indentation. The value `"tools"` is the name of the Python module (the `tools/` folder).

**Step 4.** Save the file. Verify that the YAML is valid and that no other sections were removed or broken.

**Step 5.** **In Codio**, use **Check It!** below. The grader will check that **`level5/endpoints.yml`** contains a `tools:` key and `tools_module: "tools"`.

{Check It!|assessment}(code-output-compare-501030001)
