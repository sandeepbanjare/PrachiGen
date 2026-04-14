import streamlit as st
import google.generativeai as genai

# 1. Yahan apni API Key hamesha " " ke andar hi rakhein
API_KEY = "AIzaSyBlKXwwGmVQ1BwNg34wH59yxc2dfFpkfS4"
import streamlit as st
import google.generativeai as genai

# 1. Yahan apni API Key hamesha " " ke andar hi rakhein
API_KEY = import streamlit as st
import google.generativeai as genai

# 1. Yahan apni API Key hamesha " " ke andar hi rakhein
API_KEY = ""import streamlit as st
import google.generativeai as genai

# 1. Yahan apni API Key hamesha " " ke andar hi rakhein
API_KEY = "YAHAN_APNI_KEY_DAALO" 

# 2. AI Model Setup
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

# 3. Website ka Look (UI)
st.set_page_config(page_title="PrachiGen AI", page_icon="🚀")
st.title("PrachiGen: Creator's Growth Engine")
st.write("Ab har video hogi Viral! 🚀")

# 4. User Input
topic = st.text_input("Apni video ka topic ya idea likho:", placeholder="e.g. Minecraft Survival Hindi")

# 5. Button click hone par kya hoga
if st.button("Magic Karo"):
    if topic:
        with st.spinner('PrachiGen dimaag laga raha hai...'):
            try:
                # AI ko instruction dena
                prompt = f"Identify trending hooks, a viral script, and 3 high-CTR thumbnail ideas for a YouTube video about: {topic}. Respond in a friendly and professional way."
                response = model.generate_content(prompt)
                
                # Result dikhana
                st.subheader("🔥 Aapka Viral Plan Taiyar Hai:")
                st.write(response.text)
                st.success("Best of luck for your video!")
            except Exception as e:
                st.error(f"Kuch galti hui: {e}")
    else:
        st.warning("Bhai, pehle topic toh likh lo!")
 

# 2. AI Model Setup
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

# 3. Website ka Look (UI)
st.set_page_config(page_title="PrachiGen AI", page_icon="🚀")
st.title("PrachiGen: Creator's Growth Engine")
st.write("Ab har video hogi Viral! 🚀")

# 4. User Input
topic = st.text_input("Apni video ka topic ya idea likho:", placeholder="e.g. Minecraft Survival Hindi")

# 5. Button click hone par kya hoga
if st.button("Magic Karo"):
    if topic:
        with st.spinner('PrachiGen dimaag laga raha hai...'):
            try:
                # AI ko instruction dena
                prompt = f"Identify trending hooks, a viral script, and 3 high-CTR thumbnail ideas for a YouTube video about: {topic}. Respond in a friendly and professional way."
                response = model.generate_content(prompt)
                
                # Result dikhana
                st.subheader("🔥 Aapka Viral Plan Taiyar Hai:")
                st.write(response.text)
                st.success("Best of luck for your video!")
            except Exception as e:
                st.error(f"Kuch galti hui: {e}")
    else:
        st.warning("Bhai, pehle topic toh likh lo!")


# 2. AI Model Setup
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

# 3. Website ka Look (UI)
st.set_page_config(page_title="PrachiGen AI", page_icon="🚀")
st.title("PrachiGen: Creator's Growth Engine")
st.write("Ab har video hogi Viral! 🚀")

# 4. User Input
topic = st.text_input("Apni video ka topic ya idea likho:", placeholder="e.g. Minecraft Survival Hindi")

# 5. Button click hone par kya hoga
if st.button("Magic Karo"):
    if topic:
        with st.spinner('PrachiGen dimaag laga raha hai...'):
            try:
                # AI ko instruction dena
                prompt = f"Identify trending hooks, a viral script, and 3 high-CTR thumbnail ideas for a YouTube video about: {topic}. Respond in a friendly and professional way."
                response = model.generate_content(prompt)
                
                # Result dikhana
                st.subheader("🔥 Aapka Viral Plan Taiyar Hai:")
                st.write(response.text)
                st.success("Best of luck for your video!")
            except Exception as e:
                st.error(f"Kuch galti hui: {e}")
    else:
        st.warning("Bhai, pehle topic toh likh lo!")

# 2. AI Model Setup
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

# 3. Website ka Look (UI)
st.set_page_config(page_title="PrachiGen AI", page_icon="🚀")
st.title("PrachiGen: Creator's Growth Engine")
st.write("Ab har video hogi Viral! 🚀")

# 4. User Input
topic = st.text_input("Apni video ka topic ya idea likho:", placeholder="e.g. Minecraft Survival Hindi")

# 5. Button click hone par kya hoga
if st.button("Magic Karo"):
    if topic:
        with st.spinner('PrachiGen dimaag laga raha hai...'):
            try:
                # AI ko instruction dena
                prompt = f"Identify trending hooks, a viral script, and 3 high-CTR thumbnail ideas for a YouTube video about: {topic}. Respond in a friendly and professional way."
                response = model.generate_content(prompt)
                
                # Result dikhana
                st.subheader("🔥 Aapka Viral Plan Taiyar Hai:")
                st.write(response.text)
                st.success("Best of luck for your video!")
            except Exception as e:
                st.error(f"Kuch galti hui: {e}")
    else:
        st.warning("Bhai, pehle topic toh likh lo!")
          
