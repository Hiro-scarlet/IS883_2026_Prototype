import streamlit as st
from transformers import pipeline

# Page configuration
st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="💬"
)

st.title("💬 Sentiment Analyzer")
st.write("Enter some text below and analyze its sentiment.")

# Load the model
@st.cache_resource
def load_model():
    return pipeline(
        "text-classification",
        model="cardiffnlp/twitter-roberta-base-sentiment-latest"
    )

pipe = load_model()

# Text input
text = st.text_area(
    "Enter your text:",
    placeholder="e.g., I really enjoyed this course!",
    height=150
)

# Analyze button
if st.button("Analyze Sentiment"):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        result = pipe(text)[0]

        label = result["label"]
        score = result["score"]

        st.subheader("Result")

        if label.lower() == "positive":
            st.success(f"**Sentiment:** {label}")
        elif label.lower() == "negative":
            st.error(f"**Sentiment:** {label}")
        else:
            st.info(f"**Sentiment:** {label}")

        st.write(f"**Confidence:** {score:.1%}")
