import streamlit as st
import pickle
import re

# -------------------------------
# Load model and vectorizer
# -------------------------------
model = pickle.load(open("models/model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

# -------------------------------
# Label mapping
# -------------------------------
label_map = {
    0: "Politics",
    1: "Technology",
    2: "Entertainment",
    3: "Business"
}

# -------------------------------
# Text cleaning function
# -------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="News Classifier", page_icon="📰")

st.title("📰 News Category Classifier")
st.write("Enter a news article and get its category")

# Input box
user_input = st.text_area("Enter news text here:")

# Button
if st.button("Classify"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        # Clean input
        cleaned = clean_text(user_input)

        # Convert to TF-IDF
        vector = vectorizer.transform([cleaned])

        # Predict
        prediction = model.predict(vector)[0]

        # Show result
        st.success(f"Predicted Category: {label_map[prediction]}")

        # Optional: confidence
        try:
            prob = model.predict_proba(vector).max()
            st.info(f"Confidence: {prob:.2f}")
        except:
            pass

# Footer
st.markdown("---")
st.markdown("Built using Machine Learning & NLP 🚀")