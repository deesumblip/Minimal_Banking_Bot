Once you have a `tools/` module with tool functions, you must **register** it with Rasa so the assistant can discover and call them.

## endpoints.yml

Add a **tools** section to `endpoints.yml`:

```yaml
tools:
  tools_module: "tools"
```

This tells Rasa to load the Python module named `tools` (the `tools/` folder with `__init__.py` and your banking_tools.py). Rasa will discover any functions listed in `__all__` in that module and make them available to the LLM.

Do not remove or change the existing sections (action_endpoint, nlg, model_groups). Just add the `tools:` block. In Lab 3.1 you will add this section and verify the agent can load the tools.
