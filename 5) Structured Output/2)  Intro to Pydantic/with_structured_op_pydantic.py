from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from pydantic import Field, BaseModel
from typing import Literal, Optional


class review(BaseModel):
    keythemes: list[str] = Field(description="Write down all the key themes discussed in the review as List")
    summary: str =Field(description="Brief Summary of the Review")
    sentiment: Literal["positive","negative","neutral"] =  Field(description="analyse whether the review is positive , negative or neutral")
    pros: Optional[list[str]]= Field(description="Write down all the Pros inside a list", default=None)
    cons: Optional[list[str]] = Field(description="Write down all the Cons inside a list", default=None)
    name: Optional[str] = Field(default=None, description="Write the name of the Reviewer")


model = ChatGoogleGenerativeAI(
     model="gemini-2.5-flash",
    temperature=0.9
)

structured_model = model.with_structured_output(review)

res = structured_model.invoke("""I had the most incredible dining experience at this restaurant! The food was absolutely delicious - every dish was perfectly prepared and beautifully presented. Our server was attentive, knowledgeable, and made excellent recommendations. The atmosphere was elegant yet comfortable. I can't wait to come back and try more items from their menu. Definitely a new favorite spot!""")

print(res)
print(res.name)