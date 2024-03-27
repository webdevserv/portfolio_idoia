"""
@author: idoia lerchundi
"""
import gradio as gr
import urllib.request
from PIL import Image
import streamlit as st

from PIL import Image

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
   page_title="Streamlit iCodeIdoia",
   page_icon="images/ilpicon1.png",layout="wide",initial_sidebar_state="expanded"
)

st.image("images/banner.jpg")

# ---- LOAD
local_css("styles/style.css")
#openai.api_key = "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"

#original it was working
#openai.api_key = "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"

gr.load("models/stabilityai/stable-diffusion-xl-base-1.0").launch('share=True')

#OPENAI_API_KEY = "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"
#openai.api_key = os.getenv(OPENAI_API_KEY)
#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



st.subheader('Stable Diffusion XL 1.0')
st.caption("Testing.")
# text input box for image recognition
img_description = st.text_input('Enter image prompt. e.g. hyperrealistic, female web developer coding on a full moon night, back view, wide angle lens')

#if st.button('Generate Image'):    
    #generated_img = generate_image(img_description)
    #st.image(generated_img)