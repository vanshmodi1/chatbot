from dotenv import load_dotenv
load_dotenv()

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st


# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user."),
        ("user", "Question: {question}")
    ]
)


# Streamlit
st.title("LangChain Demo With Gemma")

input_text = st.text_input("Search the topic you want")


# Ollama Gemma LLM
llm = OllamaLLM(model="gemma:latest")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser


if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)