import os
from pathlib import Path
from landingai_ade import LandingAIADE, APIConnectionError, RateLimitError
import landingai_ade
# from dotenv import load_dotenv
import streamlit as st
from functools import lru_cache

@lru_cache(maxsize=1)
def get_landing_client() -> LandingAIADE:
    """Initialize and cache the Landing AI ADE client."""
    api_key = st.secrets["LANDING_API_KEY"]
    return LandingAIADE(apikey=api_key, environment="eu")

def pdf_parser_func(pdf_path: str) -> str:
    """
    Parse a PDF file into markdown using Landing AI ADE.
    Returns the parsed markdown text.
    """
    if not pdf_path or not Path(pdf_path).is_file():
        raise FileNotFoundError(f"Invalid or missing PDF path: {pdf_path}")

    client = get_landing_client()

    try:
        response = client.parse(document=Path(pdf_path), model="dpt-2-latest")
        return getattr(response, "markdown", "").strip()
    except APIConnectionError as e:
        st.error("Unable to reach Landing AI servers. Please check your connection.")
        print(f"Connection error: {e.__cause__}")
    except RateLimitError:
        st.warning("Rate limit reached. Please wait before retrying.")
    except Exception as e:
        st.error(f"Unexpected error while parsing PDF: {e}")

    return ""