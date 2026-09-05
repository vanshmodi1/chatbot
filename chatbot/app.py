from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LangSmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user", "Question: {question}")
    ]
)

# Streamlit framework
st.title("LangChain Chatbot")
input_text = st.text_input("Enter your question here:")

# OpenAI LLM
llm = ChatOpenAI(model="gpt-4o-mini")

# Output parser
output_parser = StrOutputParser()

# Chain
chain = prompt_template | llm | output_parser

# Run chain
if input_text:
    st.write(chain.invoke({"question": input_text}))