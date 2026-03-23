### Your Task

Train your bot so that it includes your actions and flows. You must run the training command **from inside the `level2` folder** (so Rasa finds `config.yml`, `endpoints.yml`, and your domain/data).

1. **Activate the virtual environment** (e.g. `source .venv/bin/activate` on Codio/Linux, or `.venv\Scripts\Activate.ps1` on Windows PowerShell). Your prompt should show `(.venv)`.
2. **Go into `level2`:** run `cd level2`.
3. **Run training:**
   ```bash
   python -m rasa train
   ```

Wait for training to finish. A model file (`.tar.gz`) will be created in `level2/models/`.

---

### Verification

Before submitting, confirm:

- Training completed without errors
- A model file exists under `models/`

**Use Check It!** below when done (Codio).

{Check It!|assessment}(code-output-compare-1070925386)
