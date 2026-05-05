**Starting point:** Work in **`level4/`** with a trained model from **Lab 5.1**.

From `level4/` with the virtual environment active:

```bash
python -m rasa inspect --debug --log-file logs/logs.out
```

### What you are testing

This unit adds `ask_before_filling` on the `account` collect step in `transfer_money`. Run through the conversation in order, at step 6, Rasa asks for the account number again even though you provided it in step 2. `check_balance` persisted the slot, but `ask_before_filling: true` overrides it, ensuring account numbers for financial transactions are always confirmed explicitly.

| Step | You type | What to notice |
|------|----------|----------------|
| 1 | `What's my balance?` | Agent asks for your account number |
| 2 | `123456` | Agent returns a balance. The `account` slot is now persisted. |
| 3 | `I'd like to transfer some money` | Agent enters the transfer flow |
| 4 | `200 dollars` | `amount` fills immediately, agent asks for recipient |
| 5 | `Alice` | `recipient` fills, agent asks for account |
| 6 | `123456` | Rasa asks again, it does not reuse the persisted value |
| 7 | *(read only)* | `action_process_transfer` fires: **Transfer of $200 from account 123456 to Alice has been processed successfully.** |

### Try it with upfront information

Type `/restart` in Inspector to reset the conversation, then try giving Rasa multiple pieces of information in a single message:

> `I'd like to transfer $50 to Alice`

Rasa extracts `amount` and `recipient` from that message and skips straight to asking for the account number. This is the default slot-filling behaviour. The LLM command generator reads the whole message and fills whatever slots it can. Only `account` is held back, because `ask_before_filling: true` prevents it from being filled without an explicit question.

Try a few variations: include only the amount, only the recipient, or neither. Each time, Rasa asks only for what is still missing.