import streamlit as st
import google.generativeai as genai

# 1. API Key (Apni key quotes ke andar dalo)
API_KEY = "AIzaSyBlKXwwGmVQ1BwNg34wH59yxc2dfFpkfS4"

genai.configure(api_key=API_KEY)

# 2. MODEL KA NAAM UPDATE (Iski wajah se error aa raha tha)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="PrachiGen AI", page_icon="🚀")
st.title("PrachiGen: Creator's Growth Engine")
st.write("Video Topic dalo aur Viral content pao!")

topic = st.text_input("Apni video ka idea likho:")

if st.button("Magic Karo"):
    if topic:
        with st.spinner('PrachiGen soch raha hai...'):
            try:
                prompt = f"Give a viral hook, script, and thumbnail ideas for: {topic}"
                response = model.generate_content(prompt)
                st.subheader("Aapka Viral Plan:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Pehle kuch likho toh sahi!")
              
