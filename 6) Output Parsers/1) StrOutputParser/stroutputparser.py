from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.9
)

template1 = PromptTemplate(
    template="explain me about the {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="Summarize the content in 5 lines: {content}",
    input_variables=['content']
)

prompt1 = template1.invoke({
    'topic':'cricket'
})

res = model.invoke(prompt1)

prompt2 = template2.invoke({
    'content':res.content
})

summary = model.invoke(prompt2)

print(summary.content)