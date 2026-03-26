**Starting point:** Work in **`level5/`** (see **Unit 0.1**).

Before moving to **Chapter 1.6** (or beyond), ensure you can:

- Explain the difference between **tools** (LLM selects at runtime) and **actions** (explicitly called in flows)
- Create a **`tools/`** module with Python functions and export them via **`__all__`**
- Add a **`tools:`** section to **`endpoints.yml`** with **`tools_module: "tools"`**
- Create a flow that collects slots and runs an action in a context where the LLM can call tools
- Create an action class with **`name()`** and **`run()`** that reads slots and returns events (and understand that the LLM can invoke tools in that context)
- **Train** from **`level5/`** with the venv activated at **project root** (**`python -m rasa train`**) and pass the **completion check** (**Lab 5.2**)
- Optionally **test** **`transfer_money_tools`** in **Rasa Inspector** and confirm tool-calling behavior

If you can do all of the above, you are ready for Chapter 1.6 or for extending your agent with more tools and flows.
