# Agents:
- Through this component we can easily create AI agents.
- We know that LLMs are Capable of Context Aware Text Generation and Natural Language Understanding Ability, using this chatbots can be created.
## Difference betweem ChatBots and AI Agents:
- For example, consider chatbot in Travel Website, in this we can just ASK questions like "what is best place to visit in India during Summer?"
- As Chatbots are powered by LLMs,  which is trained on datas on Internet , at the time pof training, it would have got infos lie  "Shimal is best place to visit during summer", so it just replies based on the Data which it had been trained (data from the internet)
- Consider if ther was an AI agent instead of Chat Bots, if we ask question like "Tell me the cheapest Flight to Delhi on 24th of october", the query hits the AI agent through API , it retrieves the answer and tells, the output of which flight is of chapest rate.
- we can also ask like, "book the flight"
- it has capability to Book Flights by going to websites!
- This is the main difference between the ChatBot and AI agent.
- AI agent is just ChatBot with Super Powers

## AI Agents:
- Two thing that it has which Cahtbot lacks:
 - - 1) Reasoning Capabilities.
 - - 2) It has access to Tools to do things. 
- With these both capabilities, AI agents does its job.
- lets say we have given AI agent acces to  
 - - 1) Calculator
 - - 2) Access to Weather API, so that it can get info about knowledge of Weather condition of any weather at any time.
#### There are many techniques for Reasoning, one of them is Chain OF Thoughts
- in this, the user Query is divided into multiple parts
- the LLM thinks , how to complete each part of the Query so that the whole mentioned task is completed!
- for example consider an User query "Multiply 3 with Current Temperature in Kokota"
- AI breaks down the Query into parts like : "Get the current Temperatur value in Kolkota" ; "Multiply it by 3"
- The AI searches it tools, finds Weather API, gets the output value for Temperature in Kolkota
- in order to complete the second task, again it searches it tools, find calculator, then LLM provides input as the temperature that it got from Weather API, then the Number 3 then teh operation Multiplication as input the the calculator tool
- the output of this is displayed as output.
  