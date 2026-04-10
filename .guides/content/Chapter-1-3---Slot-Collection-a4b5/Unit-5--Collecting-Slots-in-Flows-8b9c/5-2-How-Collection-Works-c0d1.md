**Section 1.3** walked through the first time the flow hits a `collect:` step: ask if empty, store the reply, then continue. This section adds the usual reason the agent **does not** ask again.

If the `account` slot **already holds a value** from an earlier turn in the conversation, Rasa skips `utter_ask_account` and goes straight to the next step. The action still runs with the slot value that is already in the tracker.

That is how a follow-up like "What's my balance?" can resolve without re-prompting for the account number. The slot persisted.

{Check It!|assessment}(multiple-choice-5130520013)
