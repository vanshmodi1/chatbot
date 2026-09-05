import requests
import streamlit as st


# =========================
# ESSAY API
# =========================

def get_essay_response(input_text):
    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json={
            "input": {
                "topic": input_text
            }
        }
    )

    return response.json()["output"]


# =========================
# POEM API
# =========================

def get_poem_response(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={
            "input": {
                "topic": input_text
            }
        }
    )

    return response.json()["output"]


# =========================
# STREAMLIT UI
# =========================

st.title("LangChain Demo with Ollama Gemma API")

input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write a poem on")


# Essay
if input_text:
    st.write(get_essay_response(input_text))


# Poem
if input_text1:
    st.write(get_poem_response(input_text1))