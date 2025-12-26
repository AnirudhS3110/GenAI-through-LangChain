from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from typing import TypedDict

model = ChatGoogleGenerativeAI(
     model="gemini-2.5-flash",
    temperature=0.9
)

class review(TypedDict):
    summary:str
    sentiment:str

model_with_structured_op = model.with_structured_output(review)

res = model_with_structured_op.invoke("""I had the most incredible dining experience at this restaurant! The food was absolutely delicious - every dish was perfectly prepared and beautifully presented. Our server was attentive, knowledgeable, and made excellent recommendations. The atmosphere was elegant yet comfortable. I can't wait to come back and try more items from their menu. Definitely a new favorite spot!""")

print(res)
print(type(res))