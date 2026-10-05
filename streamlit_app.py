import streamlit as st
from google import genai
from google.genai import types

### Load your API Key
try:
    gemini_api_key = st.secrets['MyGeminiKey']
except (KeyError, FileNotFoundError):
    st.error("No Gemini key found. Add `MyGeminiKey` under **Manage app → ⋮ → Settings → Secrets**, then refresh this page.")
    st.stop()

client = genai.Client(api_key=gemini_api_key)

MODEL = "gemini-3.1-flash-lite"

st.write("Press the button to say hello")

# Language selection
language = st.radio(
    "Select a language:",
    ["English", "Japanese", "Spanish"]
)

# Generate greeting
if st.button("Press me!"):
    prompt = f"Say hello in one full sentence in {language}."
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )
    st.write(response.text)
