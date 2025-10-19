import google.generativeai as genai
import os
# from dotenv import load_dotenv
import streamlit as st
from functools import lru_cache

@lru_cache(maxsize=1)
def get_gemini_model():
    """Initialize and cache the Gemini model."""
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    return genai.GenerativeModel("gemini-2.0-flash")

def generate_content(prompt: str) -> str:
    """Generate text content using Gemini LLM."""
    if not prompt or not isinstance(prompt, str):
        raise ValueError("Prompt must be a non-empty string.")
    llm = get_gemini_model()
    response = llm.generate_content(prompt)
    return response.text.strip() if hasattr(response, "text") else ""