"""
@author: idoia lerchundi
"""
#import urllib.request
from PIL import Image,ImageFile
import streamlit as st
#import requests
#from io import BytesIO
from rembg import remove

st.set_page_config(
   page_title="Streamlit iCodeIdoia",
   page_icon="images/icon.png",layout="wide",initial_sidebar_state="expanded"
)

st.image("images/banner.jpg")

#Input and output as bytes
def remove_bg(input_path):
 output_path = 'output.png'

 with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        feedback = o.write(output)
        display_progress(feedback)

 return output_path

def display_progress(output):
   st.write(output)

def main():     
 st.subheader("Remove Background from image")

 uploaded_file = st.file_uploader("Upload an image. e.g. Select 1_for_super_resolution.jpg from sample folder.", type=['png', 'jpg', 'jpeg', 'gif'])
 if uploaded_file is not None:
    #PIL            
    lr_image = Image.open(uploaded_file)
    st.text("Your Uploaded Image")
    st.image(lr_image)
    st.text("Please wait a few seconds. Monitor top right of your screen.")

    if st.button('Remove background'):                               
        #filename = uploaded_file.name
        #hardcoded upload folder
        filepath = "C:/Users/idoia/OneDrive/CAREER/github/portfolio_idoia/samples/"
        #print("filepath " + filepath)
        #print("filename " + filename)
        imagepath = filepath + uploaded_file.name
        generated_img = remove_bg(imagepath)
        st.text("Image background removed.")
        #st.text("ESRGAN image saved sucessfully, as *SuperResolutionFile.jpg.")              
        
        st.image(generated_img)  


if __name__ == "__main__":
    main()