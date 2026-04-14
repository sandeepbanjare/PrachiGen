import streamlit as st
import google.generativeai as genai

# 1. API Key (Apni key yahan dalo)
API_KEY =  "AIzaSyBlKXwwGmVQ1BwNg34wH59yxc2dfFpkfS4"

genai.configure(api_key=API_KEY)

# 2. Ye code sabse best model apne aap chun lega
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="PrachiGen AI", page_icon="🚀")
st.title("PrachiGen: Creator's Growth Engine")

topic = st.text_input("Apni video ka idea likho:")

if st.button("Magic Karo"):
    if topic:
        with st.spinner('PrachiGen process kar raha hai...'):
            try:
                # Direct response call
                response = model.generate_content(topic + " ke liye viral youtube script aur thumbnail idea do")
                st.subheader("Aapka Viral Plan:")
                st.write(response.text)
            except Exception as e:
                # Agar flash nahi mila toh purana pro try karega
                try:
                    alt_model = genai.GenerativeModel('gemini-pro')
                    response = alt_model.generate_content(topic)
                    st.write(response.text)
                except:
                    st.error(f"Google Server Error: {e}. Please check your API Key in Google AI Studio.")
    else:
        st.warning("Pehle kuch likho toh sahi!")
              
