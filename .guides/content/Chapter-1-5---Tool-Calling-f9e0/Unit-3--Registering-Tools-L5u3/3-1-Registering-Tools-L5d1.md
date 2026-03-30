**Starting point:** Work in **`level5/`** after **Labs 2.0 and 2.1** (**`prompt_template`**, **`tools/banking_tools.py`**, **`__all__`**). This page explains how to **register** the tools module in **`endpoints.yml`**; **Lab 3.1** applies it.

With a **`tools/`** module in place, **register** it so Rasa can load and expose those functions to the LLM.

## `level5/endpoints.yml`

Add a **`tools`** section to **`level5/endpoints.yml`**:

```yaml
tools:
  tools_module: "tools"
```

This points Rasa at the Python package **`tools`** (the **`tools/`** folder with **`__init__.py`** and **`banking_tools.py`**). Functions listed in **`__all__`** become available to the LLM.

Leave **`action_endpoint`**, **`nlg`**, and **`model_groups`** as they are; **append** the **`tools:`** block. **Lab 3.1** has you save this and run the code check.
