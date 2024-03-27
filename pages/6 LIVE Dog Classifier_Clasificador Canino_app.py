"""
@author: idoia lerchundi
"""
import urllib.request
from PIL import Image,ImageFile
import streamlit as st
import numpy as np
import requests
from io import BytesIO
###################

from fastai.vision.widgets import *
from fastai.vision.all import *
from pathlib import Path

import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
   page_title="Streamlit iCodeIdoia",
   page_icon="images/ilpicon1.png",layout="wide",initial_sidebar_state="expanded"
)
class Predict:
    def __init__(self, filename):
        self.learn_inference = load_learner(Path()/filename)
        self.img = self.get_image_from_upload()
        if self.img is not None:
            self.display_output()
            self.get_prediction()
    
    @staticmethod
    def get_image_from_upload():
        uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg', 'jpg'])
        #if uploaded_file is not None:
            #return PILImage.create((uploaded_file))
        #return None


        st.subheader("Square an image app")
        img_description = st.text('Image will be squared with color filler where applicable.')
        uploaded_file = st.file_uploader("Upload a JPG image to square and fill with color.", type=['jpg'])

        if uploaded_file is not None: 
             img = Image.open(uploaded_file)
             img.load()
             st.image(img.to_thumb(500,500), caption='Uploaded Image')
             get_prediction(img)
             #generated_img = fill_square_image(img)
             #st.image(generated_img)
        return None




    def display_output(smallimage):
        st.image(smallimage.img.to_thumb(500,500), caption='Uploaded Image')

    def get_prediction(imagetopredict):

        if st.button('Classify'):
            pred, pred_idx, probs = imagetopredict.learn_inference.predict(imagetopredict.img)
            st.write(f'Prediction: {pred}; Probability: {probs[pred_idx]:.04f}')
        else: 
            st.write(f'Click the button to classify') 

if __name__=='__main__':

    file_name='pkl/dog.pkl'

    predictor = Predict(file_name)




######################

file_name="pkl/dog.pkl"
st.image("images/banner.jpg")

# ---- LOAD
local_css("styles/style.css")
