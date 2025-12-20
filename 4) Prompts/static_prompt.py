from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

st.header("Research Tool")

user_input = st.text_input("Enter your prompt")

if st.button("Click!"):
    if user_input and user_input.strip():
        result = llm.invoke(user_input)
        st.write(result.content)
    else:
        st.warning("Please enter a prompt")
