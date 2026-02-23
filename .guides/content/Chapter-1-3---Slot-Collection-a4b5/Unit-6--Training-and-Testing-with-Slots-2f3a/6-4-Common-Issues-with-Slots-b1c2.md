## Issue. Slot Not Collected

**Symptoms.** The bot doesn't ask for the slot value.

**Possible causes.** The slot is not defined in the domain. The `collect:` step is missing or incorrect. The `utter_ask_*` response is missing.

**Solutions.** Check the `slots:` section in the domain. Verify the flow has a `collect: account` step. Ensure the `utter_ask_account` response exists.

## Issue. Slot Always None in Action

**Symptoms.** The action reads the slot but gets `None`.

**Possible causes.** The slot was not collected before the action runs. The user didn't provide a value. There is a slot name mismatch.

**Solutions.** Ensure the `collect:` step comes before the action in the flow. Check that the user actually provided a value. Verify the slot name matches exactly (case-sensitive).
