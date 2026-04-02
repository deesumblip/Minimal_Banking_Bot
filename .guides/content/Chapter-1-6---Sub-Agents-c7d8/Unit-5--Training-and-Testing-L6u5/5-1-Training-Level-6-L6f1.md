## 5.1 Training (Lab 5.1)

After Labs 2.1–4.1, train the Level 6 assistant from **`level6/`** so the model package includes the sub-agent, **`mcp_servers`** in **`endpoints.yml`**, and the **`ask_banking_assistant`** flow. Use the **same** virtual environment as the rest of the course (typically **`.venv`** at the **repo root**).

### Step 1 — Train

Open a terminal. From **project root**, activate the venv, change to **`level6/`**, then run **`rasa train`**. Wait until training finishes; a model is written under **`level6/models/`**.

```bash
# Windows (PowerShell or CMD): .venv\Scripts\activate
source .venv/bin/activate

cd level6
rasa train
```

### Step 2 — Lab 5.1 (graded, Codio)

Use **Check It!** below after training completes. The grader verifies training (e.g. model directory or success indicator).

{Check It!|assessment}(code-output-compare-501060004)

Graded **Check It!** runs in the **Codio** guide; you can still train locally with the commands in Step 1.
