# JSON Output Parser:
- You cant enforce Schema in which the LLM gives an ouput Using JSON output parser, It is decided by the LLM.

### Example:
```python
from langchain_core.output_parsers import JsonOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate


llm = HuggingFaceEndpoint(
    model="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name , age City of a fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={
        'format_instruction':parser.get_format_instructions()
    }
)

template.format()

prompt = template.invoke({})

res = model.invoke(prompt)

json = parser.parse(res.content)

print(json)

print(type(json))
```
Output:
```
{'name': 'Aisha Khan', 'age': 28, 'city': 'London'}
<class 'dict'>
``` 
- Here we can see that the parser has converted the Output from the LLM as a dictionary

### Improvised Code with chain:

```python
from langchain_core.output_parsers import JsonOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate


llm = HuggingFaceEndpoint(
    model="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name , age City of a fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={
        'format_instruction':parser.get_format_instructions()
    }
)

chain = template | model | parser

res = chain.invoke({})

print(res)
```
Output:
```
{'name': 'Anya Petrov', 'age': 27, 'city': 'Berlin, Germany'}
```
