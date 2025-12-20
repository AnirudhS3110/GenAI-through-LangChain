# Prompts:
- THese are input instructions or Queries given to a model to guide to its output
## Two types of PRompts:
- Static
- Dynamic

### Static:
- Static Prompts are we feed into LLM without modifying teh USer's input.
- Not used much, as we are giving the User More control in Our Application in terms of Prompting, this is because LLM's output is directly dependent upon the Given input to it.
- If a user gives a wrong topic name. The LLM will give output for teh wrong topic, which could lead to Hallucination
- We need to provide a Consistent User Experience to the User from using our LLM app, static prompting doesnt help it

### Dynamic Orompts:
- These are Templased based or Structured Prompts.
- Example: <br>
![alt text](image-1.png)

### Prompt Template:
- A PromptTemplate in LangChain is a structured way to create prompts dynamically by inserting variables into a predefined template
- nstead of
hardcoding prompts, PromptTemplate allows you to define placeholders that can be filled in at runtime with different inputs.
- Instead of hardcoding prompts, PromptTemplate allows you to define placeholders that can be filled in at runtime with different inputs.

### Why USe Prompt Templates?
- It does Validation of Input Data by default, to activate this, we need to use ```validate_template=True```
- These are **REUSABLE**: Using this we can write the prompt as F-Strings and convert it into json file through ```prompt.save(filename)``` as in <a href="./prompt_generator.py">click</a>
- **Highly coupled with LangChain Ecosystem**: We can use Prompts Easily integrated with Chains!