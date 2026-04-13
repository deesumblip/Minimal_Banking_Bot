**Starting point:** Work in **`level5/`** with **Labs 2.0 and 2.1** complete (**`data/prompts/`**, **`prompt_template`**, **`tools/banking_tools.py`**, **`__all__`**).

**Objective.** The prior page showed the **`tools:`** block for **`endpoints.yml`**. Here you add it to **`level5/endpoints.yml`** so Rasa loads the tools from **Lab 2.1**.

## Step-by-Step Instructions

**Step 1.** Confirm **`level5/tools/__init__.py`** exists (from Lab 2.1). Rasa imports **`tools`** as a package. Missing **`__init__.py`** can break registration.

**Step 2.** Open **`level5/endpoints.yml`**. Leave **`action_endpoint`**, **`nlg`**, and **`model_groups`** intact.

**Step 3.** Add a **`tools`** section (for example after **`action_endpoint`** or before **`model_groups`**):

```yaml
tools:
  tools_module: "tools"
```

Use 2-space indentation. The value `"tools"` is the name of the Python module (the `tools/` folder).

**Step 4.** Save. Confirm the file is valid YAML and other sections are untouched.

**Step 5.** **In Codio**, run **Check It!** below. The grader expects a top-level **`tools:`** with **`tools_module: "tools"`**.

{Check It!|assessment}(code-output-compare-501030001)
