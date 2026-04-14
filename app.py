import streamlit as st
import google.generativeai as genai

# API Key yahan dalo
API_KEY = "AIzaSyBlKXwwGmVQ1BwNg34wH59yxc2dfFpkfS4"

genai.configure(api_key=API_KEY)

st.title("PrachiGen AI 🚀")

# Model list check karne ke liye (sirf testing ke liye)
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
    st.success("AI Model Ready!")
except Exception as e:
    st.error(f"Model Load Nahi Hua: {e}")

topic = st.text_input("Video Idea:")

if st.button("Magic Karo"):
    if topic:
        try:
            response = model.generate_content(topic)
            st.write(response.text)
        except Exception as e:
            st.error(f"Galti: {e}")
  
