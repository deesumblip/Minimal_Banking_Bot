### 0.1 Your Level 1 Banking Bot

Before we add actions, let's recap what you've already built in Level 1. **All of this remains unchanged** - Level 2 builds on top of it!

#### What You Have from Level 1

**Domain File (`domain/basics.yml`)**:
- ✅ `utter_greet` - Greets users as a banking assistant
- ✅ `utter_help` - Lists banking services (balance, transfers, hours, contact)
- ✅ `utter_contact` - Provides bank contact information
- ✅ `utter_goodbye` - Says goodbye when the user ends the conversation

**Flows (`data/basics/`)**:
- ✅ `greet.yml` - Greets users when they start a conversation
- ✅ `help.yml` - Explains what the bot can help with
- ✅ `contact.yml` - Provides contact information for the bank
- ✅ `goodbye.yml` - Says goodbye when the user ends the conversation

**System Patterns (`data/system/patterns/patterns.yml`)**:
- ✅ `pattern_session_start` - Automatically greets users when conversation begins
- ✅ `pattern_completed` - Handles flow completion

**Configuration Files**:
- ✅ `config.yml` - Bot configuration (pipeline, policies)
- ✅ `credentials.yml` - Connection settings
- ✅ `endpoints.yml` - Action endpoints and LLM configuration

#### What Level 1 Couldn't Do

Your Level 1 bot was limited to **static responses** - predefined text that never changes. It couldn't:
- ❌ Execute custom Python code
- ❌ Perform calculations
- ❌ Access databases or APIs
- ❌ Return dynamic responses based on conditions
- ❌ Process data or make decisions

**Example**: If a user asked "What are your bank hours?", your Level 1 bot would need a static `utter_hours` response. It couldn't check the current day or calculate if the bank is currently open.

---
