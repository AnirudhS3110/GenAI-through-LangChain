from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.9
)


 
con = Console()

chat_history= [
    SystemMessage(content='You are a helpful Assitant')
]

while True:
    inp = input("You: ")
    chat_history.append(HumanMessage(content=inp))
    if inp == 'exit':
        break
    res = model.invoke(chat_history)
    chat_history.append(AIMessage(content=res.content))
    con.print('AI: ', Markdown(res.content))
con.print(chat_history)