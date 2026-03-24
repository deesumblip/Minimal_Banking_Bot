### 6.2 How to Train Your Agent

**What you'll do**: In **Lab 6.1** you'll run the training command, see what success looks like, and fix common errors. The lab is split into **Part 1: In Codio** and **Part 2: Running locally**. Follow the part that matches your setup.

**Why run training now**: You've built domain and flows; the next step is to turn them into a model so you can actually talk to the agent in Inspector. Training is the gate between "I edited files" and "the agent runs." Once it succeeds, you'll have a model file you can use for testing and demos.

**Command** (from the `level1` folder with venv active):
```bash
python -m rasa train
```

**Success**: You should see "Successfully saved model to 'models/...'" and a new `.tar.gz` file in `models/`.

---
