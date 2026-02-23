# 0.1 Your Level 2 Banking Bot

Before we add slots (memory), here is a quick recap of what you built in Level 2. All of this remains unchanged. Level 3 builds on top of it.

The **level3** folder is set up as a copy of your Level 2 bot. In this chapter you will add slots and an ask response in the domain, register the new action (its file is provided), and create the check_balance flow. Everything else is your Level 2 content.

## What You Have from Level 2

**Domain File (`domain/basics.yml`)**. You have all Level 1 responses (`utter_greet`, `utter_help`, `utter_contact`), and often `utter_goodbye`, plus an `actions:` section with `action_bank_hours` registered. If you added `action_holiday_hours` in Level 2, your domain may list that too.

**Flows (`data/basics/`)**. You have the Level 1 flows (`greet`, `help`, `contact`), the Level 2 flow `hours` that uses `action_bank_hours`, and if you did Level 2 Lab 5.1, `holiday_hours` as well.

**Actions (`actions/`)**. You have `action_bank_hours.py` and, if you built it in Level 2, `action_holiday_hours.py`. The Level 3 folder also contains `action_check_balance_simple.py` (provided). You will register that action in the domain in Lab 3.1.

**System Patterns and Configuration**. Unchanged from Level 2.

## What Level 2 Couldn't Do

Your Level 2 bot could execute custom Python code, but it could not remember information from the conversation, store user-provided data, use information from earlier in the conversation, or ask for missing information and remember it.

**Example.** If a user asked "Check my balance", your Level 2 bot could not remember which account the user has, ask for the account number and remember it, or use that account number in subsequent actions.
