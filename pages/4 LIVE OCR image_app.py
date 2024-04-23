"""
@author: idoia lerchundi
"""
import urllib.request
from PIL import Image,ImageFile
import streamlit as st
import numpy as np
import requests
from io import BytesIO
import easyocr as ocr 

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
   page_title="Streamlit iCodeIdoia - OCR an IMAGE - Extract text from an image",
   page_icon="images/ilpicon1.png",layout="wide",initial_sidebar_state="expanded"
)

st.image("images/banner.jpg")

# ---- LOAD
local_css("styles/style.css")

@st.cache_resource
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 

reader = load_model() #load model

# ---- TABS
tab1, tab2 = st.tabs(["Demo","Application"])

with tab1:   
   # Handle first image
   
   url = "https://https://raw.githubusercontent.com/webdevserv/images_video/main/ocr_sample.jpg" 

   st.subheader("OCR an image demo")
   img_description = st.text('Image text will extracted using OCR.')

   if st.button('OCR Demo'):  
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    st.image(input_image) #display image
    img.load()

    with st.spinner("🔄 OCR in process."):
        result = reader.readtext(np.array(img))
        result_text = [] #empty list
        for text in result:
            result_text.append(text[1])

        st.write(result_text)
    st.balloons()
   else:
    st.write("Upload an image to extract text using OCR.")

   
with tab2:
  st.subheader("OCR an image app")
  img_description = st.text('Image text will be extracted using OCR.')
  uploaded_file = st.file_uploader("Upload a image to OCR.", type=['jpg'])

  if uploaded_file is not None: 
   img = Image.open(uploaded_file)
   img.load()

   with st.spinner("🔄 OCR in process."):
        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results
        
        for text in result:
            result_text.append(text[1])

        st.write(result_text)
   st.balloons()
  else:
   st.write("Upload an image to extract text using OCR.")
