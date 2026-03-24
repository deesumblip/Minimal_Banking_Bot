### 0.2 Project Structure

Understanding the file structure will help you navigate the codebase and understand how everything fits together.

**Why we have this layout**: Rasa expects a specific layout so it can find your domain, flows, and config. When you add a response or a flow, you'll know exactly where it goes. When something breaks, you'll know which file to open. Think of it as a map: once you know where things live, building and debugging become straightforward.

#### Complete File Tree

```
level1/
├── config.yml              # How to build the agent (pipeline, policies)
├── credentials.yml         # How to connect (REST, Socket.IO)
├── endpoints.yml           # Where to find actions/LLMs
├── .env                    # Environment variables (secrets - not committed)
├── domain/
│   └── basics.yml          # Agent knowledge base (responses)
├── data/
│   ├── basics/             # User-facing flows (conversation scripts)
│   │   ├── greet.yml
│   │   ├── help.yml
│   │   └── contact.yml
│   └── system/
│       └── patterns/
│           └── patterns.yml # System patterns (session start, completed)
└── models/                 # Generated during training (don't edit)
```

#### File Purpose Overview

**Configuration Files** (root level):
- **`config.yml`**: Defines how Rasa builds your agent (which LLM to use, which policies, etc.)
- **`credentials.yml`**: Defines how the agent connects to chat interfaces
- **`endpoints.yml`**: Defines where to find custom actions and LLM configurations

**Domain Files** (`domain/`):
- **`domain/basics.yml`**: The agent's knowledge base - defines all responses the agent can say

**Flow Files** (`data/`):
- **`data/basics/*.yml`**: User-facing conversation scripts (flows)
- **`data/system/patterns/patterns.yml`**: System-level behaviors (session start, flow completion)

**Generated Files** (created automatically):
- **`models/`**: Compiled agent models (created when you run `rasa train`)
- **`logs/`**: Log files for debugging

#### How Files Work Together

```
User sends message
    ↓
config.yml (defines how to understand it)
    ↓
data/*.yml (flows define what to do)
    ↓
domain/basics.yml (responses define what to say)
    ↓
Agent responds
```

**Key Relationships**:
- **Flows** (in `data/`) reference **Responses** (in `domain/`)
- **Config** tells Rasa how to process everything
- **System patterns** control conversation lifecycle

---
