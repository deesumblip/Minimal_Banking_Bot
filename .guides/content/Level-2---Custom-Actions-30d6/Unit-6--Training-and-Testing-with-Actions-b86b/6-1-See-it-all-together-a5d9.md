Now that level 2 has come to an end, you should be able to explain how custom actions differ from static responses, describe the structure of an `Action` class and how it is registered in the domain, and use a custom action in a flow. 

## What your Rasa agent can do so far

```
[New session starts]
pattern_session_start triggers automatically
  Flow: pattern_session_start
  Step: utter_greet
Agent: "Hi! I'm a banking assistant. How can I help you today?"

[User: "What are your hours?"]
Rasa matches: hours flow
  Step: action_bank_hours (checks current day via datetime)
Agent: "Today is Saturday, we're open 10am-2pm." (or full weekday schedule)

[User: "What are your holiday hours?"]
Rasa matches: holiday_hours flow
  Step: action_holiday_hours (checks if today is a holiday via datetime)
Agent: "We're closed today for Christmas." (or general holiday schedule)

[User: "How can I contact you?"]
Rasa matches: contact flow
  Step: utter_contact (static response)
Agent: "You can reach us at support@bank.com or call 1-800-BANK-123."
```

**Test your knowledge:** 


{Check It!|assessment}(multiple-choice-1208100001)

{Check It!|assessment}(multiple-choice-1208100002)

{Check It!|assessment}(multiple-choice-1208100003)

{Check It!|assessment}(multiple-choice-1208100004)

{Check It!|assessment}(multiple-choice-1208100005)



You've officially completed Level 2, great job! 

![Great Job](.guides/img/L2_minions_excited.gif)

Start Level 3 next to add memory to your agent. 
