"""
@author: idoia lerchundi
"""
import urllib.request
from PIL import Image,ImageFile
import streamlit as st
import numpy as np
import requests
from io import BytesIO
from streamlit_component_fill_square_cropper import fill_square_cropper as imported_fill_square_cropper

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

# ---- TABS
tab1, tab2 = st.tabs(["Demo","Application"])

with tab1:   
   # Handle first image
   url = "https://raw.githubusercontent.com/webdevserv/images_video/main/cowportrait.jpg" 
   # Handle second image
   url2 = "https://raw.githubusercontent.com/webdevserv/images_video/main/cowlandscape.jpg"

   st.subheader("Square an image demo")
   img_description = st.text('Image will be squared with color filler where applicable.')

   if st.button('Square and Fill Demo'):  
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.load()

    generated_img = imported_fill_square_cropper(img)
    st.image(generated_img)

    response = requests.get(url2)
    img = Image.open(BytesIO(response.content))
    img.load()

    generated_img = imported_fill_square_cropper(img)
    st.image(generated_img)
   
with tab2:
  st.subheader("Square an image app")
  img_description = st.text('Image will be squared with color filler where applicable.')
  uploaded_file = st.file_uploader("Upload a JPG image to square and fill with color.", type=['jpg'])

  if uploaded_file is not None: 
   img = Image.open(uploaded_file)
   img.load()
   generated_img = imported_fill_square_cropper(img)
   st.image(generated_img)