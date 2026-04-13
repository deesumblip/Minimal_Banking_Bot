Understanding the file structure will help you navigate the codebase and understand how everything fits together. The diagram below shows the file tree **at the beginning of the course**. As you progress, you will add pieces such as **sub-agents** and **tools** implemented as **actions**.

---

## Complete File Tree

```text
level1/
├── config.yml # How to build the agent (pipeline, policies)
├── credentials.yml # How to connect (REST, Socket.IO)
├── endpoints.yml # Where to find actions/LLMs
├── .env # Environment variables (manually added locally)
├── domain/
│   └── basics.yml # Agent knowledge base (responses)
├── data/
│   ├── basics/ # User-facing flows (conversation scripts)
│   │   ├── greet.yml
│   │   ├── help.yml
│   │   └── contact.yml
│   └── system/
│       └── patterns/
│           └── patterns.yml # System patterns (session start, completed)
├── logs/ # Log files (e.g. when running Inspector; may be empty at first)
└── models/ # Generated during training (don't edit)
```

The layout above is the **starter** Level 1 agent before most labs. As you work through the chapter you will add more flows and domain responses. After you run **`rasa train`**, a packaged model appears under **`models/`**.

The tree lists only the **agent** files. Your real **`level1/`** folder may also include course notes as **`.md`** files, helper scripts, **`.guides`**, **`.rasa`**, and other items. Those extras support the course; they are not part of the agent definition above.

**Note for Codio Students**: Credentials are pre-configured via environment variables. The `.env` file may not be visible in your project; that's expected.

---

## File Purpose Overview

### Configuration Files (root level)

- **`config.yml`**: Defines how Rasa builds your agent (which LLM to use, which policies, etc.)
- **`credentials.yml`**: Defines how the agent connects to chat interfaces
- **`endpoints.yml`**: Defines where to find custom actions and LLM configurations

### Domain Files (`domain/`)

- **`domain/basics.yml`**: The agent's knowledge base, defines all responses the agent can say

### Flow Files (`data/`)

- **`data/basics/*.yml`**: User-facing conversation scripts (flows)
- **`data/system/patterns/patterns.yml`**: System-level behaviors (session start, flow completion)

### Generated Files (created automatically)

- **`models/`**: Compiled agent models (created when you run `rasa train`)
- **`logs/`**: Log files for debugging

---

## How Files Work Together

```text
User sends message
↓
config.yml (defines how to understand it)
↓
data/.yml (flows define what to do)
↓
domain/basics.yml (responses define what to say)
↓
Agent responds
```

### Key Relationships

- **Flows** (in `data/`) reference **Responses** (in `domain/`)
- **Config** tells Rasa how to process everything
- **System patterns** control the conversation lifecycle

{Check It!|assessment}(multiple-choice-2989489112)