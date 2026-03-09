### 6.1 What is Training?

**Training** is the process of building your bot's "brain" - converting your flows, domain, and configuration into a runnable model.

**Why we train**: Until you run training, Rasa only has your YAML files. It doesn't yet have a single artifact it can load to answer users. Training reads all of that and produces a model file. Every time you change the domain or flows, you need to train again so the model reflects your latest design. No training means the bot can't run, or it runs an old version.

#### What Happens During Training

When you run `rasa train`, Rasa:

1. **Reads all flows** from the `data/` folder: it scans `.yml` files, parses flow definitions, and builds a flow graph.
2. **Reads the domain** from the `domain/` folder and loads all responses, plus slots and actions when present.
3. **Applies configuration** from `config.yml`: pipeline, policies, language.
4. **Creates a model file** and saves it to `models/` with a timestamped name such as `20250112-120817-descent-lard.tar.gz`. This is the "compiled" version of your bot.

**Analogy**: Training is like compiling code. Your flows/domain are source code; training creates the executable.

---
