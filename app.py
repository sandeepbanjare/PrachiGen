import streamlit as st
import google.generativeai as genai

# 1. API Key (Hamesha quotes " " ke andar)
API_KEY = "AIzaSyBlKXwwGmVQ1BwNg34wH59yxc2dfFpkfS4" # <-- Yahan apni puri key paste karo

# 2. Setup
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

# 3. UI Design
st.set_page_config(page_title="PrachiGen AI", page_icon="🚀")
st.title("PrachiGen: Creator's Growth Engine")
st.write("Video Topic dalo aur Viral content pao!")

# 4. Input aur Button
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
      
