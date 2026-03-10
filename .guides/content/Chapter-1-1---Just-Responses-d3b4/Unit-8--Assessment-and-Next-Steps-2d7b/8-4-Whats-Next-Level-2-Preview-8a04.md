Level 2 **builds on your existing Level 1 bot** (same domain, same flows; no new bot).

**Level 2 adds**: Custom Python actions; new flows that use actions; action registration in the domain (`actions:` section).

**Example**: "What are your bank hours?" – Level 1 would need a static response; Level 2 uses `action_bank_hours` (Python) for dynamic hours. You'll create the action class, register it, and add a flow that calls it.
