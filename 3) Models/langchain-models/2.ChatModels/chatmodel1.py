from langchain_openai import ChatOpenAI
from dotenv  import load_env

load_env()

model = ChatOpenAI(model="gpt-4", temperature=0.3, max_completion_tokens=10) # MAx completion Tokens we can set, that thisn is the maximum number of token length upto whicn the model can provide the output

res = model.invoke("What is today's date?")

print(res.content)