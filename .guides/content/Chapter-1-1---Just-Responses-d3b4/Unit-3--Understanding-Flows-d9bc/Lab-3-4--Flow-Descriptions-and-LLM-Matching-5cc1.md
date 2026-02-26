### Lab 3.4: Flow Descriptions and LLM Matching

**Objective**: Create new flows with good descriptions that help the LLM match user messages.

**Before You Begin**:
- ✅ You've completed Lab 3.2 (created goodbye.yml)
- ✅ You understand flow structure (flows:, name:, description:, steps:)
- ✅ You know where `data/basics/` folder is located
- ✅ You can reference existing flows (greet.yml, goodbye.yml) as templates

#### Understanding Flow Descriptions

The `description` field is **critical** because the LLM uses it to match user messages to flows.

**How It Works**:
1. User sends a message: "What are your hours?"
2. LLM reads all flow descriptions
3. LLM matches the message to the best-fitting description
4. Rasa triggers that flow

**Writing Good Descriptions**:

**Good descriptions**:
- Clear and specific: "Tell the user when the bank is open and what the operating hours are"
- Action-oriented: "Provide contact information for the bank"
- Context-aware: "Explain what the bot can help with"

**Bad descriptions**:
- Too vague: "Help user" (what kind of help?)
- Too specific: "Respond when user says exactly 'hello'" (misses "hi", "hey")
- Missing context: "Say hello" (when? why?)

#### Task: Create 2 New Flows

Create 2 new flow files in `data/basics/` folder. Use `greet.yml` or `goodbye.yml` as templates for structure.

**Flow 1: Bank Hours**
- **File**: `data/basics/hours.yml`
- **Flow name**: `hours`
- **Description**: Write a clear, specific description about providing bank hours
- **Steps**: At least one action (e.g., `utter_hours` - you may need to create this response in domain/basics.yml first, or use an existing response)

**Flow 2: Account Balance Help**
- **File**: `data/basics/balance.yml`
- **Flow name**: `balance`
- **Description**: Write a clear, specific description about explaining how to check account balance
- **Steps**: At least one action (e.g., `utter_balance_help` or use an existing response)

#### Step-by-Step Instructions

1. **Create hours.yml**:
   - Copy the structure from `greet.yml` or `goodbye.yml` as a template
   - Change the flow name to `hours`
   - Write a good description (see examples below)
   - Add at least one step with an action

2. **Create balance.yml**:
   - Copy the structure from `greet.yml` or `goodbye.yml` as a template
   - Change the flow name to `balance`
   - Write a good description (see examples below)
   - Add at least one step with an action

#### Example: Good Descriptions

Here are examples of good flow descriptions for **different** flows (not the ones you're creating):

**Example 1: Contact Information Flow**:
```yaml
flows:
  contact:
    name: contact info
    description: "Provide contact information for the bank, including phone numbers and email addresses"
    steps:
      - action: utter_contact
```

**Example 2: Services Flow**:
```yaml
flows:
  services:
    name: available services
    description: "List all the services and features the bot can help with, including account management and support options"
    steps:
      - action: utter_help
```

**Key**: Be specific about what the flow does, not how the user asks for it. Notice how these descriptions:
- Use action verbs ("Provide", "List")
- Are specific about what information is given
- Include context about what the flow accomplishes
- Are at least 20 characters long

**Your Task**: Create similar descriptions for `hours.yml` and `balance.yml` following this pattern, but write your own descriptions (don't copy these examples).

#### Checklist

Before submitting, verify:
- Both files exist in `data/basics/` folder
- Both flows have `name:` fields
- Both flows have `description:` fields (at least 20 characters, specific and action-oriented)
- Both flows have `steps:` sections with at least one action
- Descriptions are unique (different from each other and from other flows)
- YAML syntax is correct (2 spaces indentation, no tabs)
- File structure matches the template (flows: at top level, proper indentation)

{Check It!|assessment}(llm-based-auto-rubric-1348023599)
