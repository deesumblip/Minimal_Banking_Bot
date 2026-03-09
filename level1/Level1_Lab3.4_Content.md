**Objective**: In Units 3.1–3.3 you saw flow structure and how descriptions help the LLM match user messages. In this lab you create two new flows (hours, balance) with clear, specific descriptions.

**Why hours and balance**: A banking assistant is expected to answer "when are you open?" and "how do I check my balance?" Adding dedicated flows for these gives the bot clear paths for two very common questions. You write the description so the LLM knows when to trigger each flow, and you add the response or responses in the domain or reference existing ones. In Lab 3.5 you'll align these with the exact content the course expects for assessment.

**Before You Begin**: You've completed Lab 3.2; you understand flow structure; you can use `greet.yml` or `goodbye.yml` as templates.

#### Task: Create 2 New Flows

**Flow 1: Bank Hours** – File: `data/basics/hours.yml`  
- Flow name: `hours`  
- Description: Clear, specific description about providing bank hours  
- Steps: At least one action, such as `utter_hours`. Add the response in the domain first if needed, or use an existing response.

**Flow 2: Account Balance Help** – File: `data/basics/balance.yml`  
- Flow name: `balance`  
- Description: Clear, specific description about explaining how to check account balance  
- Steps: At least one action, such as `utter_balance_help`, or use an existing response.

#### Checklist

- Both files exist in `data/basics/`
- Both flows have `name:` and `description:` at least 20 characters long, specific and action-oriented.
- Both have `steps:` with at least one action
- Descriptions are unique; YAML uses 2 spaces, no tabs

**AI Coach**: Ask "How do I write a good flow description?" or "What makes a description too vague?"
