### 6.1 Training: What It Does and How to Run It

**Training** is the process of building your agent's "brain" — converting your flows, domain, and configuration into a runnable model.

Until you train, Rasa only has your YAML files; it needs a packaged model to run the agent. When you change the domain or flows, train again so the model matches your latest edits. Training is the bridge between editing files and running the agent (for example in Rasa Inspector after you have a model).

#### What Happens During Training

When you run `rasa train`, Rasa:

1. **Reads all flows** from the `data/` folder: it scans `.yml` files, parses flow definitions, and builds a flow graph.
2. **Reads the domain** from the `domain/` folder and loads all responses, plus slots and actions when present.
3. **Applies configuration** from `config.yml`: pipeline, policies, language.
4. **Creates a model file** and saves it to `models/` with a timestamped name such as `20250112-120817-descent-lard.tar.gz`. This is the "compiled" version of your agent.

**Analogy**: Training is like compiling code. Your flows/domain are source code; training creates the executable.

#### What you'll do in Lab 6.1

In **Lab 6.1** you run the full sequence in the project terminal: activate the virtual environment at the project root, `cd` into `level1`, and run the training command. You'll see what success looks like and how to fix common errors.

From the `level1` folder with the venv active:

```bash
python -m rasa train
```

**Success**: Look for a line like `Successfully saved model to 'models/...'` and a new `.tar.gz` file under `models/`.

---
