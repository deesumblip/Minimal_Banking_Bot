**Objective**: Create the `check_balance.yml` flow that collects the `account` slot and then runs `action_check_balance_simple`.

## Part 1: In Codio

1. **Terminal**: From project root (`~/workspace`), run `source .venv/bin/activate`, then `cd level3`.
2. **Create** the file `data/basics/check_balance.yml` in the `level3` folder.
3. **Add** the flow (see Unit 4.2):
   - Flow name: `check_balance`
   - `name` and `description` for the flow
   - `steps:` with (1) `collect: account` (and `description: "account number"`), (2) `action: action_check_balance_simple`
4. **Verify**: File in `data/basics/`; flow has `name`, `description`, `steps`; first step is `collect: account`, second is the action.

Run the assessment when done.

## Part 2: Running locally

1. From project root, activate venv, then `cd level3`.
2. Create `level3/data/basics/check_balance.yml` with the flow structure above.
3. Verify as above.

**Success criteria**: `data/basics/check_balance.yml` exists with a flow that has `collect: account` and `action: action_check_balance_simple`.
