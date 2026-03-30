**Starting point:** Work in **`level5/`** with every lab in this chapter complete.

Before **Chapter 1.6** (or further work on this bot), you should be able to:

- Explain how **tools** (model-chosen at runtime) differ from **actions** (named in the flow)
- Add **`data/prompts/command_prompt_v3_slot_names.jinja2`** and **`prompt_template`** in **`config.yml`** (**Lab 2.0**) so the command generator uses domain slot names
- Build a **`tools/`** module, export tool functions in **`__all__`**
- Add **`tools:`** to **`endpoints.yml`** with **`tools_module: "tools"`**
- Author a flow that collects slots, runs an action in a tool-calling context, and extend **`from_llm`** so **`transfer_money_tools`** fills **amount**, **recipient**, and **account_from**
- Implement an action with **`name()`** and **`run()`** that reads slots via **`tracker.get_slot`**, calls **`dispatcher.utter_message`**, returns events, and know the LLM may still call tools in that step
- **Train** from **`level5/`** with the venv at project root (**`python -m rasa train`**) and pass the **completion check** (**Lab 5.2**)
- Optionally exercise **`transfer_money_tools`** in **Rasa Inspector** and observe tool behavior

When that list feels comfortable, you are ready for Chapter 1.6 or for adding more tools and flows on your own.
