"""
@author: idoia lerchundi 
"""
import urllib.request
from PIL import Image
import streamlit as st

from transformers import AutoModel, AutoTokenizer

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


st.subheader('Stable Diffusion XL 1.0')
st.caption("Testing.")
# text input box for image recognition
img_description = st.text_input('Enter image prompt. e.g. hyperrealistic, female web developer coding on a full moon night, back view, wide angle lens')
@st.cache(allow_output_mutation=True)
def load_model():
    model_name = "models/stabilityai/stable-diffusion-xl-base-1.0"
    model = AutoModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer

model, tokenizer = load_model()
#if st.button('Generate Image'):    
    #generated_img = generate_image(img_description)
    #st.image(generated_img)
