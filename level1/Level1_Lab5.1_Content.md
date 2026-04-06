# Lab 5.1: Configuration Exploration

**Objective**: Understand configuration files by exploring them.

**Why this lab**: When you train or run the agent, Rasa reads config to know which LLM to use and how to behave. A quick look at the config answers "what language?" and "what model?" so you're not debugging in the dark later. You're not changing anything; you're just building a mental map of where the levers are.

#### Task

Answer these questions by examining the configuration files:

1. What language is the agent configured for?
2. What LLM model is being used?
3. Where would Rasa look for custom actions?
4. What does `temperature: 0.3` mean for the LLM?

#### Answers

1. English (`language: en`)
2. **`openai-gpt-5-1`**. In **`endpoints.yml`** (under **`model_groups`**) you'll see **`model: openai-gpt-5-1`** (and the same group id in **`config.yml`** as **`model_group`**).
3. The `actions/` folder. The config uses `actions_module: "actions"` to point to it.
4. The LLM will be somewhat creative but mostly consistent. A value of 0.3 is relatively low, meaning less randomness.
