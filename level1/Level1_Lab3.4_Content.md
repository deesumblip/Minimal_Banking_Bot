# Lab 3.4: Flow Descriptions and LLM Matching

**Objective**: Create new flows with good descriptions that help the LLM match user messages.

**Before You Begin**: You've completed Lab 3.2; you understand flow structure; you can use `greet.yml` or `goodbye.yml` as templates.

#### Task: Create 2 New Flows

**Flow 1: Bank Hours** – File: `data/basics/hours.yml`  
- Flow name: `hours`  
- Description: Clear, specific description about providing bank hours  
- Steps: At least one action (e.g. `utter_hours` – add the response in domain first if needed, or use an existing response)

**Flow 2: Account Balance Help** – File: `data/basics/balance.yml`  
- Flow name: `balance`  
- Description: Clear, specific description about explaining how to check account balance  
- Steps: At least one action (e.g. `utter_balance_help` or use an existing response)

#### Checklist

- Both files exist in `data/basics/`
- Both flows have `name:` and `description:` (at least 20 characters, specific and action-oriented)
- Both have `steps:` with at least one action
- Descriptions are unique; YAML uses 2 spaces, no tabs

**AI Coach**: Ask "How do I write a good flow description?" or "What makes a description too vague?"
