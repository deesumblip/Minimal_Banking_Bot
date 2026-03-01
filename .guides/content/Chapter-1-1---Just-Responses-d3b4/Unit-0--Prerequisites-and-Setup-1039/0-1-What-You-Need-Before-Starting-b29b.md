
Before diving into building your first Rasa bot, let's make sure you have everything set up correctly.

**Prerequisites**: Python knowledge, command line familiarity, file editing, **Rasa Pro license**. Plan for 2–3 hours.

**Note for Codio Students**: Start with Lab 0.1 below to create a virtual environment and install Rasa Pro. Follow the lab to set **RASA_LICENSE** and **OPENAI_API_KEY** (e.g. via `.env` in project root or Codio environment variables) before running `rasa --version` or other Rasa commands.

**Note for Local Setup**: If you are repeating this exercise on your own machine (not in Codio), create a `.env` file in your **project root** (the folder that contains all levels used in the course) with:

   ```
   RASA_LICENSE=rasaxxx-your-license-here
   OPENAI_API_KEY=sk-your-openai-key-here
   ```
Replace the placeholder with your actual Rasa Pro license.  
**Never commit `.env` to version control.**
