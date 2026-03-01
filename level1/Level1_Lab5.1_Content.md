# Lab 5.1: Configuration Exploration

**Objective**: Understand configuration files by exploring them.

#### Task

Answer these questions by examining the configuration files:

1. What language is the bot configured for?
2. Which component is used to start flows from user messages?
3. Where would Rasa look for custom actions?
4. Where are model groups configured (if you use any external LLMs in later levels)?

#### Answers

1. English (`language: en`)
2. `NLUCommandAdapter` (starts flows based on predicted intents + `nlu_trigger`)
3. The `actions/` folder (`actions_module: "actions"`)
4. In `endpoints.yml` under `model_groups` (not used in Level 1)
