## Issue: Slot Not Collected

**Symptoms**: Bot doesn't ask for slot value

**Possible causes**:
1. Slot not defined in domain
2. `collect:` step missing or incorrect
3. `utter_ask_*` response missing

**Solutions**:
1. Check `slots:` section in domain
2. Verify `collect: account` step exists in flow
3. Ensure `utter_ask_account` response exists

## Issue: Slot Always None in Action

**Symptoms**: Action reads slot but gets `None`

**Possible causes**:
1. Slot not collected before action runs
2. User didn't provide value
3. Slot name mismatch

**Solutions**:
1. Ensure `collect:` step comes before action in flow
2. Check user actually provided a value
3. Verify slot name matches exactly (case-sensitive)
