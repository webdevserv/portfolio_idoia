"""
@author: idoia lerchundi
"""
import streamlit as st
from PIL import Image,ImageFile
import numpy as np
import requests
from io import BytesIO
from streamlit_component_fill_square_cropper101 import fill_square_cropper

#streamlit_component_fill_square_cropper101._DEBUG = True

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        

st.set_page_config(
   page_title="Streamlit iCodeIdoia",
   page_icon="images/ilpicon1.png",layout="wide",initial_sidebar_state="expanded"
)
img_art = Image.open("images/add-black-headphones-302253249.png")
st.image("images/banner.jpg")

# ---- LOAD
local_css("styles/style.css")

def main() -> None:

 # ---- TABS
 tab1, tab2, tab3 = st.tabs(["Demo","Application","Contact"])

 with tab1:   
   # Handle first image
   url = "https://raw.githubusercontent.com/webdevserv/images_video/main/cowportrait.jpg" 
   # Handle second image
   url2 = "https://raw.githubusercontent.com/webdevserv/images_video/main/cowlandscape.jpg"

   st.subheader("Fill, square an image demo")
   img_description = st.text('Image will be squared with color filler where applicable.')

   if st.button('Square and Fill Demo'):  
     response = requests.get(url)
     img = Image.open(BytesIO(response.content))
     img.load()

     generated_img = fill_square_cropper(img)
     st.image(generated_img)

     response = requests.get(url2)
     img = Image.open(BytesIO(response.content))
     img.load()

     generated_img = fill_square_cropper(img)
     st.image(generated_img)
   
 with tab2:
   st.subheader("Square an image app")
   img_description = st.text('Image will be squared with color filler where applicable.')
   uploaded_file = st.file_uploader("Upload a JPG image to square and fill with color.", type=['jpg'])

   if uploaded_file is not None: 
     img = Image.open(uploaded_file)
     img.load()
     generated_img = fill_square_cropper(img)
     st.image(generated_img)
 with tab3:
    st.subheader("Contact")
    left_column, right_column = st.columns([1,2], gap="small")
    with left_column:
        st.markdown('<a href="https://webdevserv.github.io/html_bites/dev/webdev.html">More info</a>', unsafe_allow_html=True)
    with right_column:
        #st.empty()
        st.image(img_art, width=400)   

if __name__ == "__main__":
  main()