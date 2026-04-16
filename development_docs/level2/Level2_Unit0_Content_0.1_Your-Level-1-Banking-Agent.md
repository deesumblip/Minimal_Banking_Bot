Before we add actions, let's recap what you've already built in Level 1. **All of this remains unchanged** — Level 2 builds on top of it!

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

Level 2 introduces **Actions** — custom Python code that your agent can execute. This enables:

- Dynamic responses based on calculations
- Data processing and logic
- Integration with external systems
- Custom business logic

**Your existing Level 1 agent continues to work** — Level 2 adds actions on top of it!

**Already in the project before Lab 3.1** (starter):
- `actions/` folder, `actions/__init__.py`, and `actions/action_bank_hours.py` — example action you study in Units 2–3 (the domain does not list it until **Lab 4.1**).
- No `action_holiday_hours.py` yet, no `actions:` section in `domain/basics.yml`, and no `hours.yml` / `holiday_hours.yml` — you add those in the labs below.

**What you'll build**: In **Unit 3 / Lab 3.1** you'll create your own action (**action_holiday_hours**) that uses the current date—if today is a holiday it says we're closed today, otherwise it returns the general holiday schedule. In **Lab 4.1** you'll register both actions in the domain. In **Lab 5.1** you'll create **`hours.yml`** (for the example action) and **`holiday_hours.yml`** (for your action).

**Modified Files** (as you complete the labs):
- `domain/basics.yml` — You'll add an `actions:` section and list both the example action and your action (Lab 4.1)
- `data/basics/hours.yml` — Example flow for `action_bank_hours` (Lab 5.1)
- `data/basics/holiday_hours.yml` — Flow for `action_holiday_hours` (Lab 5.1)

**Unchanged Files**:
- All Level 1 responses remain
- All Level 1 flows remain
- **Configuration** — Same **tutorial LLM** setup as Level 1 (`SearchReadyLLMCommandGenerator`, `rasa_command_generation_model`, `flow_retrieval.active: false` in `config.yml`; `https://tutorial-llm.rasa.ai` in `endpoints.yml`). Level 2’s `endpoints.yml` also defines **`action_endpoint`** so Rasa loads custom actions from the **`actions`** package.

---
