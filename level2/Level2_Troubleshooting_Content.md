# Troubleshooting Guide

## Common Issues and Solutions

### Issue: Action Not Found Error

**Symptoms**: Training error: "Action 'action_xyz' not found"

**Possible Causes**:
1. Action file doesn't exist in `actions/` folder
2. Action not registered in domain
3. Action name mismatch (domain vs. `name()` method)

**Solutions**:
1. Check `actions/action_xyz.py` exists
2. Verify `domain/basics.yml` has `- action_xyz` under `actions:`
3. Ensure `name()` returns exactly `"action_xyz"` (case-sensitive)

---

### Issue: Action Executes But No Message

**Symptoms**: Action runs but user doesn't see a message

**Possible Causes**:
1. `dispatcher.utter_message()` not called
2. Python error in action (silent failure)
3. Wrong dispatcher usage

**Solutions**:
1. Check `dispatcher.utter_message()` is called in `run()` method
2. Check for Python errors (syntax, imports)
3. Verify you're using `dispatcher.utter_message(text="...")` correctly

---

### Issue: Import Error

**Symptoms**: `ImportError: cannot import name 'Action'`

**Possible Causes**:
1. Rasa SDK not installed
2. Wrong virtual environment
3. Rasa Pro not properly installed

**Solutions**:
1. Install Rasa Pro: `python -m pip install rasa-pro`
2. Activate correct virtual environment
3. Verify installation: `python -m rasa --version`

---
