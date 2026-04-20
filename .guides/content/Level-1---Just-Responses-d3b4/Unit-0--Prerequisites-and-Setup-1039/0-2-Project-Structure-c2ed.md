Understanding the file structure will help you navigate the codebase and understand how everything fits together. The diagram below shows the file tree **at the beginning of the course**. As you progress, you will add pieces such as **sub-agents** and **tools** implemented as **actions**.

---

## Complete File Tree

```text
level1/
├── config.yml # How to build the agent (pipeline, LLMs, policies)
├── credentials.yml # How to connect (REST, Socket.IO)
├── endpoints.yml # Where to find actions/LLMs
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
├── logs/ # Generated log files (e.g. when running Inspector). 
└── models/ # Generated during training (don't edit)
```

The layout above is the **starter** Level 1 agent before most labs. As you work through the chapter you will add more flows and domain responses. After you run **`rasa train`**, a packaged model appears under **`models/`**.

---

## How Files Work Together

```text
User sends message
↓
config.yml (defines how to understand it)
↓
data/.yml (sub-agents and flows define what to do)
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