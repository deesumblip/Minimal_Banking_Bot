Before moving to Level 6 (or beyond), ensure you can:

- Explain the difference between **tools** (LLM selects at runtime) and **actions** (explicitly called in flows)
- Create a **tools/** module with Python functions and export them via **`__all__`**
- Add a **tools:** section to **endpoints.yml** with **tools_module: "tools"**
- Create a flow that collects slots and runs an action in a context where the LLM can call tools
- Create an action class with `name()` and `run()` that reads slots and sends a message (and understand that the LLM can invoke tools in that context)
- **Train** the Level 5 agent from the `level5` folder (with venv activated at project root) and run the **completion check** (Lab 5.2)
- Optionally **test** the transfer_money_tools flow in Rasa Inspector and confirm tool-calling behavior

If you can do all of the above, you're ready for Level 6 or for extending your agent with more tools and flows.
