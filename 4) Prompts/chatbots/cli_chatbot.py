from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
load_dotenv()

model = ChatGoogleGenerativeAI(
     model="gemini-2.5-flash",
    temperature=0.9
)
con = Console()

while True:
    inp = input("You: ")
    if inp=='exit':
        break
    res = model.invoke(inp)
    con.print(Markdown(res.content))
