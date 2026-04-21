Before we add actions, let's recap what you've already built in Level 1. **All of this remains unchanged.** Level 2 builds on top of it.

#### What You Have from Level 1

**Domain File (`domain/basics.yml`)**:
- `utter_greet` - Greets users as a banking assistant
- `utter_help` - Lists banking services (balance, transfers, hours, contact)
- `utter_contact` - Provides bank contact information
- `utter_goodbye` - Says goodbye when the user ends the conversation

**Flows (`data/basics/`)**:
- `greet.yml` - Greets users when they start a conversation
- `help.yml` - Explains what the agent can help with
- `contact.yml` - Provides contact information for the bank
- `goodbye.yml` - Says goodbye when the user ends the conversation

**System Patterns (`data/system/patterns/patterns.yml`)**:
- `pattern_session_start` - Automatically greets users when conversation begins
- `pattern_completed` - Handles flow completion

**Configuration Files**:
- `config.yml` - Agent configuration (pipeline, policies)
- `credentials.yml` - Connection settings
- `endpoints.yml` - Action endpoints and LLM configuration

#### What Level 1 Couldn't Do

Your Level 1 agent was limited to **static responses** - predefined text that never changes. It couldn't:
- ❌ Execute custom Python code
- ❌ Perform calculations
- ❌ Access databases or APIs
- ❌ Return dynamic responses based on conditions
- ❌ Process data or make decisions

**Example**: If a user asked "What are your bank hours?", your Level 1 agent would need a static `utter_hours` response. It couldn't check the current day or calculate if the bank is currently open.

#### What's new in Level 2

Level 2 introduces **Actions**, which are custom Python code that your agent can execute. This enables:

- Dynamic responses based on calculations
- Data processing and logic
- Integration with external systems
- Custom business logic

**Your existing Level 1 agent continues to work.** Level 2 adds actions on top of it.

**What's already in the project before Lab 3.1.** The repository includes the `actions/` folder, `actions/__init__.py`, and `actions/action_bank_hours.py`. You study this example action in Units 2 and 3. The starter domain does not list the action until you reach **Lab 4.1**.

You do not yet have `action_holiday_hours.py`, an `actions:` section in `domain/basics.yml`, or the `hours.yml` and `holiday_hours.yml` flow files. You will add those files in the labs below.

**What you'll build.** In **Unit 3** and **Lab 3.1** you will create **action_holiday_hours**, which uses the current date. If today is a holiday, the action reports that the bank is closed today. Otherwise it returns the general holiday schedule. In **Lab 4.1** you will register both actions in the domain. In **Lab 5.1** you will create **hours.yml** for the example action and **holiday_hours.yml** for your action.

**Modified files as you complete the labs**

In **Lab 4.1** you will edit `domain/basics.yml` and add an `actions:` section that lists the example action and your action.

In **Lab 5.1** you will add `data/basics/hours.yml` as the example flow for `action_bank_hours` and `data/basics/holiday_hours.yml` as the flow for `action_holiday_hours`.

**Unchanged files**

All Level 1 responses remain. All Level 1 flows remain.

**Configuration** matches Level 1’s **tutorial LLM** setup. Your `config.yml` lists `SearchReadyLLMCommandGenerator`, `rasa_command_generation_model`, and `flow_retrieval.active: false`. Your `endpoints.yml` points to `https://tutorial-llm.rasa.ai`. Level 2’s `endpoints.yml` also defines **`action_endpoint`** so Rasa loads custom actions from the **`actions`** package.

---
