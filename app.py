import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# App title and styling
st.set_page_config(page_title="Spam SMS Detector", layout="centered")
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>📩 Spam SMS Detector</h1>", unsafe_allow_html=True)

# Sample message button
if st.button("Try Sample Message"):
    st.session_state.message = "Congratulations! You've won a free cruise. Call now!"

# Text input
message = st.text_area("Enter your SMS message:", key="message")

# Predict button
if st.button("Predict"):
    if message.strip() == "":
        st.warning("Please enter a message to analyze.")
    else:
        input_vector = vectorizer.transform([message])
        prediction = model.predict(input_vector)[0]
        proba = model.predict_proba(input_vector)[0][1]  # Probability of spam

        # Display result
        if prediction == 1:
            st.error("⚠️ This message is SPAM.")
        else:
            st.success("✅ This message is NOT spam.")

        # Show probability score with color-coded feedback
        st.markdown("---")
        if proba > 0.8:
            st.warning(f"High spam probability: **{proba:.2%}**")
        elif proba > 0.5:
            st.info(f"Moderate spam probability: **{proba:.2%}**")
        else:
            st.success(f"Low spam probability: **{proba:.2%}**")