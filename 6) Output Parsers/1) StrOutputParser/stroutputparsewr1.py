from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    temperature=0.7
)

template1 = PromptTemplate(
    template="explain me about the {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="Summarize the content in 5 lines: {content}",
    input_variables=['content']
)

strOpParser = StrOutputParser()

chain = template1 | model | strOpParser | template2 | model | strOpParser

res = chain.invoke({
    'topic':'cricket'
})

print(res)
