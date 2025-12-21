from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()

model = ChatGoogleGenerativeAI(
     model="gemini-2.5-flash",
    temperature=0.9
)

messages = [
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content="Tell me about Langchain")
]

res = model.invoke(messages)

messages.append(AIMessage(content=res.content))
print(messages)