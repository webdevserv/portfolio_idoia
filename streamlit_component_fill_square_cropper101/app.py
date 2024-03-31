"""
@author: idoia lerchundi
"""
import streamlit as st
import urllib.request
from PIL import Image,ImageFile
import numpy as np
import requests
from io import BytesIO
from streamlit_component_square_fill_cropper101 import fill_square_cropper

streamlit_component_square_fill_cropper101._DEBUG = True

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

#def fill_square_cropper(img):
#    imgsz = [img.height, img.width]

#    original_size = imgsz

#    smallestsize = min(imgsz)
#    biggestsize = max(imgsz)

#    #get vertical color filler
#    avg_color_per_row = np.average(img, axis=0)
#    avg_color = np.average(avg_color_per_row, axis=0)

#    if img.height > img.width:
#      #height is bigger than width
#      area = (0, 0, img.width + (img.height - img.width),img.height)
#      cropped_img = img.crop(area)
#      newimgsz = [cropped_img.height, cropped_img.width]
    
#      newimg = Image.new('RGB', ([newimgsz[1],newimgsz[0]]), (round(avg_color[0]), round(avg_color[1]), round(avg_color[2])))

#      newpos = (img.height-img.width)
#      newpos = newpos/2
#      newimg.paste(img,(int(newpos),0))

#      return newimg

#    #vertically add color
#    if img.width > img.height: 
#      area = (0, 0, img.width, img.height+ (img.width - img.height))
#      cropped_img = img.crop(area)
#      newimgsz = [cropped_img.height, cropped_img.width]
    
#      newimg = Image.new('RGB', ([newimgsz[1],newimgsz[0]]), (round(avg_color[0]), round(avg_color[1]), round(avg_color[2])))
 
#      newpos = (img.width-img.height)
#      newpos = newpos/2
#      newimg.paste(img,(0,(int(newpos))))

#      return newimg

def main() -> None:

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

main()