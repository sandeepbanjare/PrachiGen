import streamlit as st
import google.generativeai as genai

# Yahan apni Google AI Studio wali API Key paste karna
API_KEY = AIzaSyBlKXwwGmVQ1BwNg34wH59yxc2dfFpkfS4

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="PrachiGen AI", page_icon="🚀")
st.title("PrachiGen: Creator's Growth Engine")

topic = st.text_input("Apni video ka topic likho:")

if st.button("Magic Karo"):
    if topic:
        with st.spinner('PrachiGen dimaag laga raha hai...'):
            prompt = f"Identify trending hooks, a viral script, and 3 high-CTR thumbnail ideas for a video about {topic}."
            response = model.generate_content(prompt)
            st.subheader("Aapka Viral Plan:")
            st.write(response.text)
    else:
        st.warning("Pehle topic toh likho!")
              
