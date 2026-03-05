# Lab 5.1: Configuration Exploration

**Objective**: Understand configuration files by exploring them.

#### Task

Answer these questions by examining the configuration files:

1. What language is the bot configured for?
2. What LLM model is being used?
3. Where would Rasa look for custom actions?
4. What does `temperature: 0.3` mean for the LLM?

#### Answers

1. English (`language: en`)
2. GPT-4o-mini (`model: gpt-4o-mini-2024-07-18`)
3. The `actions/` folder (`actions_module: "actions"`)
4. The LLM will be somewhat creative but mostly consistent (0.3 is relatively low, meaning less randomness)
