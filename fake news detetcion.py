import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API key not found.")
    st.stop()

genai.configure(api_key=api_key)

# Updated Gemini model
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰"
)

st.title("📰 AI Fake News Detector")

news = st.text_area(
    "Enter News Article",
    height=250
)

if st.button("Analyze News"):

    if news.strip() == "":
        st.warning("Please enter news text.")
    else:

        prompt = f"""
You are an expert fact checker.

Analyze this news article.

Article:
{news}

Provide:

1. Verdict (Real / Fake / Uncertain)

2. Confidence Score (0-100%)

3. Reasons

4. Explanation

5. Sources to verify

Return answer in clean format.
"""

        with st.spinner("Analyzing..."):

            try:

                response = model.generate_content(
                    prompt
                )

                st.success("Analysis Complete")

                st.write(response.text)

            except Exception as e:

                st.error(
                    f"Error: {e}"
                )