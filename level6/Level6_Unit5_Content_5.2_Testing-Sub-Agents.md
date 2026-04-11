## 5.2 Testing and Lab 5.2 — mirror of Level 6 guide

**Part 1 — Lab 5.2 (graded):** **`code-output-compare-501060005`** in Codio (prerequisites: Labs 2.1–4.1; Lab 5.1 recommended).

**Part 2 — Optional Inspector:** three terminals; **each** new terminal — activate venv from **project root**, **`cd level6`**, then:

1. `python mcp_server/banking.py` (URL must match **`endpoints.yml`**, e.g. **`http://127.0.0.1:8080/mcp`**)
2. `python -m rasa run actions`
3. `rasa inspect` (or `rasa run`)

Open **`http://localhost:5005/webhooks/socketio/inspect.html`**, new chat, trigger **ask banking assistant**.  

Full wording: Level 6 Unit 5 page **`5-2-Testing-Sub-Agents-L6f2`**.
