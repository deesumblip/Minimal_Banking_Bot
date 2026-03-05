### 6.1 What is Training?

**Training** is the process of building your bot's "brain" - converting your flows, domain, and configuration into a runnable model.

#### What Happens During Training

When you run `rasa train`, Rasa:

1. **Reads all flows** from `data/` folder – scans `.yml` files, parses flow definitions, builds a flow graph.
2. **Reads the domain** from `domain/` folder – loads all responses (and slots/actions when present).
3. **Applies configuration** from `config.yml` – pipeline, policies, language.
4. **Creates a model file** – saves to `models/` with a timestamped name (e.g. `20250112-120817-descent-lard.tar.gz`). This is the "compiled" version of your bot.

**Analogy**: Training is like compiling code. Your flows/domain are source code; training creates the executable.

---
