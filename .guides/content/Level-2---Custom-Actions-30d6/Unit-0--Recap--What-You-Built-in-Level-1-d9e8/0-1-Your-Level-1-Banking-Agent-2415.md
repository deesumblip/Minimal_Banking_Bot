Your Level 1 agent could only return predefined text. If a user asked "are you open right now?", the agent replied with whatever you wrote in the YAML file, regardless of the actual time or day.

Level 2 fixes this with custom actions: Python classes that run during the conversation and produce a reply at the moment it is needed.

Your Level 1 files stay unchanged. Level 2 adds three new things, in this order:

<table style="width:100%;border-collapse:collapse;margin:24px 0 28px;">
<tr style="background:transparent;border:none;">
<td style="background:#fafafa;border:1px solid #e8eaf0;border-radius:6px;padding:18px 22px;">
<p style="font-size:10px;color:#bbb;margin:0 0 6px;letter-spacing:.1em;text-transform:uppercase;">01</p>
<p style="font-weight:600;color:#080327;margin:0 0 4px;font-size:0.95em;">Write the custom action</p>
<p style="font-size:0.82em;color:#636C85;margin:0 0 6px;">Python class that runs during the conversation and produces a dynamic reply.</p>
<p style="font-family:monospace;font-size:0.82em;color:#5a17ee;margin:0;">actions/action_bank_hours.py</p>
</td>
</tr>
<tr style="background:transparent;border:none;">
<td style="text-align:center;padding:6px 0;border:none;background:transparent;">
<p style="margin:0;color:#ccc;font-size:1.1em;">↓</p>
</td>
</tr>
<tr style="background:transparent;border:none;">
<td style="background:#fafafa;border:1px solid #e8eaf0;border-radius:6px;padding:18px 22px;">
<p style="font-size:10px;color:#bbb;margin:0 0 6px;letter-spacing:.1em;text-transform:uppercase;">02</p>
<p style="font-weight:600;color:#080327;margin:0 0 4px;font-size:0.95em;">Register the name</p>
<p style="font-size:0.82em;color:#636C85;margin:0 0 6px;">Tell Rasa the custom action exists. Without this, the Python file is invisible to the conversation engine.</p>
<p style="font-family:monospace;font-size:0.82em;color:#5a17ee;margin:0;">domain/basics.yml</p>
</td>
</tr>
<tr style="background:transparent;border:none;">
<td style="text-align:center;padding:6px 0;border:none;background:transparent;">
<p style="margin:0;color:#ccc;font-size:1.1em;">↓</p>
</td>
</tr>
<tr style="background:transparent;border:none;">
<td style="background:#fafafa;border:1px solid #e8eaf0;border-radius:6px;padding:18px 22px;">
<p style="font-size:10px;color:#bbb;margin:0 0 6px;letter-spacing:.1em;text-transform:uppercase;">03</p>
<p style="font-weight:600;color:#080327;margin:0 0 4px;font-size:0.95em;">Call it from a flow</p>
<p style="font-size:0.82em;color:#636C85;margin:0 0 6px;">Incorporate the custom action into a conversation. </p>
<p style="font-family:monospace;font-size:0.82em;color:#5a17ee;margin:0;">data/basics/hours.yml</p>
</td>
</tr>
</table>

The `actions/*` folder already exists in your starter project with a working example, `action_bank_hours.py`, which you will read in the next section. You will write a second custom action, `action_holiday_hours.py`, yourself.