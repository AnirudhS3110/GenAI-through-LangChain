from typing import TypedDict, Annotated, Optional, Literal
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

class review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review as List"]
    summary: Annotated[ str, "Brief Summary of the Review"]
    sentiment: Annotated[Literal["positive","negative","neutral"], "Sentiment of the Review either negative , positive or neutral"]
    pros: Annotated[Optional[list[str]],"Write down all the Pros inside a list"]
    cons: Annotated[Optional[list[str]],"Write down all the cons inside a list"]

model = ChatGoogleGenerativeAI(
     model="gemini-2.5-flash",
    temperature=0.9
)

structured_model = model.with_structured_output(review)

res = structured_model.invoke("""I had the most incredible dining experience at this restaurant! The food was absolutely delicious - every dish was perfectly prepared and beautifully presented. Our server was attentive, knowledgeable, and made excellent recommendations. The atmosphere was elegant yet comfortable. I can't wait to come back and try more items from their menu. Definitely a new favorite spot!""")

print(res)