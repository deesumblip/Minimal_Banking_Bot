# Level 1 (Ollama): Just Responses — Free Local LLM

This is the **Level 1 banking bot** configured to use **Ollama** as the LLM. No OpenAI (or other cloud) API key or sign-up is required; only a **Rasa Pro license** and a local Ollama install are needed.

## What This Folder Is

- **Same behavior as Level 1**: responses only (greet, help, contact, goodbye), no slots, no custom actions.
- **Different LLM**: uses **Ollama** (local, free, no API key) instead of OpenAI.
- **Use case**: run the bot without providing an OpenAI key; good for labs or air-gapped environments.

---

## Beginner-friendly: which path should I take?

| If you… | Do this |
|--------|--------|
| **Use Windows or macOS on your own computer** | **Easiest:** Install Ollama from [ollama.com](https://ollama.com) (download → run the installer). Then do the rest of this README (venv, Rasa Pro, `.env`). No terminal needed for Ollama. |
| **Use Codio** | **Option A is not available** — Codio runs Linux, so there’s no “download the installer” option. Use **Option B** in Step 5 (user-space install). See the Codio note there about RAM/limits; if Ollama isn’t practical, use **level1** with OpenAI instead. |
| **Use Linux (not Codio) and can’t use sudo** | Use **Option B** in Step 5 (user-space Ollama install). |
| **Don’t want to install anything extra (no Ollama)** | Use the main **level1** folder with an OpenAI API key instead. You’ll need a free OpenAI account and to set `OPENAI_API_KEY`. |
| **Get stuck** | Check that Python is 3.10 or 3.11, that your `.env` has `RASA_LICENSE=...` with no quotes, and that Ollama is running (`ollama serve` or the app open). Ask your instructor or see the main project docs. |

---

## Prerequisites (before you start)

Install these on your machine:

| Prerequisite | Purpose |
|--------------|---------|
| **Python 3.10 or 3.11** | Required for Rasa Pro. Check with `python --version` or `py -3.11 --version`. |
| **Ollama** | Local LLM server. There is **no pip install** for the server itself (the `ollama` PyPI package is only a Python client). Install the server from [ollama.com](https://ollama.com) or use the Codio-friendly steps below. |
| **Rasa Pro license** | You need a license key (e.g. [Rasa Developer Edition](https://rasa.com/docs/learn/quickstart/pro)); set it as `RASA_LICENSE` in a `.env` file in this folder. |

No OpenAI account or API key is required.

---

## Setup from scratch (virtual environment inside level1_ollama)

Do this once to create a virtual environment and install everything inside **level1_ollama**.

### 1. Go into this folder

```bash
cd level1_ollama
```

(Use the full path if needed, e.g. `cd c:\Users\YourName\Github\Rasa\Minimal_Banking_Bot\level1_ollama`.)

### 2. Create the virtual environment

**Windows (PowerShell):**
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
py -3.11 -m venv .venv
.venv\Scripts\activate.bat
```

**macOS / Linux:**
```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

You should see `(.venv)` (or similar) in your prompt. All following commands assume this venv is activated.

### 3. Upgrade pip and install Rasa Pro

**Windows:**
```powershell
python -m pip install --upgrade pip
python -m pip install --no-cache-dir rasa-pro
```

**macOS / Linux:**
```bash
pip install --upgrade pip
pip install --no-cache-dir rasa-pro
```

### 4. Set your Rasa Pro license

Create a file named `.env` in this folder (`level1_ollama`) with one line:

```text
RASA_LICENSE=rasaxxx-your-license-here
```

Replace `rasaxxx-your-license-here` with your actual Rasa Pro license. No quotes, no spaces around `=`.

**Loading the license when you run the bot**

- **Windows (PowerShell):** Before training or running, load the env file (e.g. run from this folder):
  ```powershell
  Get-Content .env | ForEach-Object { if ($_ -match '^RASA_LICENSE=(.+)$') { [Environment]::SetEnvironmentVariable('RASA_LICENSE', $matches[1].Trim(), 'Process') } }
  ```
  Or set `RASA_LICENSE` in System → Environment Variables so it’s always available.

- **macOS / Linux:** From the `level1_ollama` folder:
  ```bash
  set -a; source .env; set +a
  ```

### 5. Install and run Ollama (one-time)

The bot needs the **Ollama server** (the binary that serves the LLM). There is **no pip install** for the server: the `pip install ollama` package is only a Python client for talking to an already-running Ollama server; it does not run the model. Install the server using one of the options below.

#### Option A: Easiest — Windows or macOS on your own computer (not in Codio)

**Not in Codio:** Codio runs Linux in the cloud, so the “download and run installer” flow below doesn’t apply there. If you’re in Codio, use **Option B** instead.

- **Windows / macOS:** Download and install from [ollama.com](https://ollama.com). Run the installer; then in a terminal run `ollama pull llama3.2`.
- **Linux on your own machine (with sudo):**
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```

#### Option B: Codio / Linux without sudo (user-space install)

On **Codio** or other Linux environments where you don’t have root, you can install Ollama in your home directory:

```bash
mkdir -p ~/opt/ollama
cd ~/opt/ollama
curl -L https://ollama.com/download/ollama-linux-amd64.tgz -o ollama-linux-amd64.tgz
tar -xzf ollama-linux-amd64.tgz
export PATH="$HOME/opt/ollama:$PATH"
# Optional: make PATH permanent for this user
echo 'export PATH="$HOME/opt/ollama:$PATH"' >> ~/.bashrc
```

Then start the server and pull the model (run in a terminal you can leave open, or in the background):

```bash
ollama serve &
ollama pull llama3.2
```

**Codio note:** Codio boxes may have limited RAM or restrict long-running processes. If Ollama isn’t available or practical on your Codio instance, use **level1** with an OpenAI API key instead; **level1_ollama** is best for local machines or environments where you can run the Ollama server.

#### After the server is installed (any option above)

- Pull the model used by this bot: `ollama pull llama3.2`
- Ensure the Ollama server is running (default API: `http://localhost:11434/v1`). On Codio, if the server runs on a different host/port, set `api_base` in `endpoints.yml` accordingly (e.g. `http://localhost:11434/v1`).

---

## Quick Start (after setup)

Once the venv is created, Rasa Pro is installed, `RASA_LICENSE` is set, and Ollama has `llama3.2`:

1. **Activate the virtual environment** (if it isn’t already):
   - Windows: `.\.venv\Scripts\Activate.ps1`
   - macOS/Linux: `source .venv/bin/activate`

2. **Load `RASA_LICENSE`** (if not set system-wide), e.g. source your `.env` as in step 4 above.

3. **Train the bot:**
   ```bash
   rasa train
   ```

4. **Run the bot:**
   ```bash
   rasa run
   ```

5. **Open the Inspector** (in another terminal, with venv activated and `RASA_LICENSE` set):
   ```bash
   rasa inspect --debug --log-file logs/logs.out
   ```
   Then use the Inspector UI to chat.

---

## Configuration

| File | Role |
|------|------|
| `config.yml` | Pipeline uses `model_group: ollama-llm`. |
| `endpoints.yml` | Defines `ollama-llm` with `provider: ollama`, `api_base: http://localhost:11434/v1`, `model: llama3.2`. |
| `domain/basics.yml` | Responses (no slots/actions). |
| `data/basics/*.yml` | Flows: greet, help, contact. |
| `data/system/patterns/patterns.yml` | Session start and completion patterns. |

---

## Using a Different Ollama Model

Edit `endpoints.yml` and change the `model` under `ollama-llm` to any model you have pulled, e.g.:

- `llama3.2` (default in this project)
- `mistral`
- `phi3`
- `gemma2`

Use the same name as in `ollama pull <model>`.

---

## No OpenAI Key

You do **not** need:

- `OPENAI_API_KEY`
- Any cloud LLM account or sign-up

You **do** need:

- `RASA_LICENSE` (for Rasa Pro)
- Ollama installed and a model pulled (e.g. `llama3.2`)

---

## Relation to `level1`

- **level1**: Same bot, uses OpenAI (`gpt-4o-mini`); requires `OPENAI_API_KEY` and typically a shared venv at project root.
- **level1_ollama**: Same bot, uses Ollama; no LLM key. Includes instructions to create a **venv inside this folder** and install prerequisites from scratch.
