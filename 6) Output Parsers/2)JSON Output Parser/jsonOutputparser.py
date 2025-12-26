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