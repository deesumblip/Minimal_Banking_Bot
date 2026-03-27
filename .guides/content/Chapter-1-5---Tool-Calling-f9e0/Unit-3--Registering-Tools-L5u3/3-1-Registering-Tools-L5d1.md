**Starting point:** Work in **`level5/`** after **Lab 2.1** ( **`tools/banking_tools.py`** and **`__all__`** ). This page shows how to **register** that module in **`endpoints.yml`**; the **lab that follows** this page is where you apply it.

Once you have a **`tools/`** module with tool functions, you must **register** it with Rasa so the assistant can discover and call them.

## `level5/endpoints.yml`

Add a **`tools`** section to **`level5/endpoints.yml`**:

```yaml
tools:
  tools_module: "tools"
```

This tells Rasa to load the Python module named **`tools`** (the **`tools/`** folder with **`__init__.py`** and **`banking_tools.py`**). Rasa discovers any functions listed in **`__all__`** in that module and makes them available to the LLM.

Do **not** remove or change the existing sections (**`action_endpoint`**, **`nlg`**, **`model_groups`**). Add only the **`tools:`** block. The **lab that follows** has you add this section and verify the agent can load the tools.
