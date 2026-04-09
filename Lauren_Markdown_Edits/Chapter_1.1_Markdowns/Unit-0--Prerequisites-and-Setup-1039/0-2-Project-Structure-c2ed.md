Understanding the file structure will help you navigate the codebase and understand how everything fits together. This is the file tree at the beginning of the course. Items like **sub-agents** and **tools (actions)** will be added to the file tree as you progress through the course. 

---

## Course File Tree

```
level1/
├── config.yml # How to build the agent (pipeline, policies)
├── credentials.yml # How to connect (REST, Socket.IO)
├── endpoints.yml # Where to find actions/LLMs
├── .env # Environment variables (manually added locally)
├── domain/
│ └── basics.yml # Agent knowledge base (responses)
├── data/
│ ├── basics/ # User-facing flows (conversation scripts)
│ │ ├── greet.yml
│ │ ├── help.yml
│ │ └── contact.yml
│ └── system/
│ └── patterns/
│ └── patterns.yml # System patterns (session start, completed)
└── models/ # Generated during training (don't edit)
```

**Note for Codio Students**: Credentials are pre-configured via environment variables. The `.env` file may not be visible in your project; that's expected.

---

## File Purpose Overview

### Configuration Files (root level)

- `**config.yml`**: Defines how Rasa builds your agent (which LLM to use, which policies, etc.)
- `**credentials.yml**`: Defines how the agent connects to chat interfaces
- `**endpoints.yml**`: Defines where to find custom actions and LLM configurations

### Domain Files (`domain/`)

- `**domain/basics.yml**`: The agent's knowledge base—defines all responses the agent can say

### Flow Files (`data/`)

- `**data/basics/*.yml**`: User-facing business processes (flows)
- `**data/system/patterns/patterns.yml**`: System-level behaviors (session start, flow completion)

### Generated Files (created automatically)

- `**models/**`: Compiled agent models (created when you run `rasa train`)
- `**logs/**`: Log files for debugging

---

## How Files Work Together

```
User sends a message
   ↓
config.yml (Defines how to undertand it and orchestrate to right user journey)
   ↓
data/flows (Houses all the possible flows)
   ↓
Does the flow call a sub-agent agent?
   ├── YES → Help user with sub-agent (ReAct)
   │         ↓
   │     sub-agents/ (autonomous reasoning + tool use)
   │         ↓
   │     ✅ Generates its own response (domain/ NOT required)
   │
   └── NO → Help user with a flow
             ↓
         data/flows/ (pre-defined business process + tool use)
             ↓
         domain/basics.yml (defines the possible responses)
             ↓
         ✅ Responds to user (rephrased or templated from domain/)
```

### Key Relationships

- **Flows** (in `data/`) reference **Responses** (in `domain/`)
- **Config** defines how Rasa should orchestrate everything all together
- **System patterns** control the conversation lifecycle

{Check It!|assessment}(multiple-choice-2989489112)

{Check It!|assessment}(multiple-choice-1308821528)