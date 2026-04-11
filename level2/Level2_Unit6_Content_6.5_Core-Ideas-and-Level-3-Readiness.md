**Level 3 Unit 0** already walks through what stays in your project, what Level 2 could not do (no durable memory across turns), and how slots and the **`check_balance`** path fit together. Read that when you want the full handoff. This page is a short **Level 2** checkpoint only.

#### Core ideas and what you can do now

You should be solid on how **actions** differ from static **responses**, how an **Action** class is structured and registered in the domain, how the **dispatcher** sends messages from **`run()`**, and how Rasa runs actions from flows. In labs you added **`action_holiday_hours`**, registered it, and wired **`holiday_hours`** alongside **`hours`** / **`action_bank_hours`**. The **Check It!** items on **6.4** (*See it all together*) exercise those ideas.

#### What Level 2 still does not cover

Without **slots**, the agent does not reliably retain user-specific facts (for example an account reference) from one turn to the next. Level 3 adds that layer. Multi-field and tool-centric patterns appear in later chapters when your design needs them.

#### Readiness before Level 3

- You can explain what an action is and how it differs from a response.
- You created **`action_holiday_hours`** in Lab 3.1 and see how it fits next to the example action.
- **`action_bank_hours`** and **`action_holiday_hours`** appear under **`actions:`** in the domain where required, and you have the **`hours`** and **`holiday_hours`** flows.
- You know how actions are triggered from flows and how to spot failures in Inspector or logs.

If those points feel true, continue to **Level 3 Unit 0** for the Level 3 recap and setup.

---
