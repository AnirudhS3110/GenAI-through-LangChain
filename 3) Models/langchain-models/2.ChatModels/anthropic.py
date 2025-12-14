from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

model = ChatAnthropic(model="claude-sonnet-4-5-20250929")

print(model.invoke("What is today's date").content)