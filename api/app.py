from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from langserve import add_routes

from dotenv import load_dotenv
import uvicorn


# Load environment variables
load_dotenv()


# Create FastAPI app
app = FastAPI(
    title="LangChain API",
    version="1.0",
    description="Multiple routes using LangChain, FastAPI and Ollama"
)


# =========================
# OLLAMA MODEL
# =========================

llm = OllamaLLM(
    model="gemma:latest"
)


# =========================
# PROMPT 1 - ESSAY
# =========================

prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words"
)


# =========================
# PROMPT 2 - POEM
# =========================

prompt2 = ChatPromptTemplate.from_template(
    "Write me a poem about {topic} with 100 words"
)


# =========================
# ROUTE 1 - ESSAY
# =========================

add_routes(
    app,
    prompt1 | llm,
    path="/essay"
)


# =========================
# ROUTE 2 - POEM
# =========================

add_routes(
    app,
    prompt2 | llm,
    path="/poem"
)


# =========================
# RUN SERVER
# =========================

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="localhost",
        port=8000
    )