"""
@author: idoia lerchundi
"""
import urllib.request
from PIL import Image,ImageFile
import streamlit as st
import numpy as np
import requests
from io import BytesIO

#pip install rembg[gpu]
#pip install rembg

from rembg import remove

#input_path = 'input.png'
output_path = 'output.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)

def remove_bg(input_path):

#input_path = 'input.png'
 output_path = 'output.png'

 with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)

 st.image(output_path)

# Streamlit execution starts in main() function.
def main():     
 st.subheader("Enhanced Super Resolution GAN Process Single Image - TensorFlow implementation")
#readme_text.empty()
 uploaded_file = st.file_uploader("Upload a low resolution JPG image. e.g. Select 1_for_super_resolution.jpg from sample folder.", type=['jpg'])
 if uploaded_file is not None:            
    lr_image = Image.open(uploaded_file)
    st.text("Your Uploaded Image")
    st.image(lr_image)
    time_message="Please wait a few seconds. Monitor top right of your screen."
    st.text(time_message)
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

















#import os
color=(0,0,255)
st.image("images/banner.jpg")

def fill_square_image(img):
    imgsz = [img.height, img.width]

    original_size = imgsz
    #print("original image")
    #img = Image.open(img)
    #display(img)
    #print('size is ')
    #display(imgsz)

    smallestsize = min(imgsz)
    biggestsize = max(imgsz)

    #get vertical color filler
    avg_color_per_row = np.average(img, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)

    if img.height > img.width:
      #print("height is bigger than width")
      area = (0, 0, img.width + (img.height - img.width),img.height)
      cropped_img = img.crop(area)
      #print("area is")
      #print(area)
      newimgsz = [cropped_img.height, cropped_img.width]
    
      #round(avg_color)
      #print("round avg_color")
      #print(round(avg_color[0]))
      newimg = Image.new('RGB', ([newimgsz[1],newimgsz[0]]), (round(avg_color[0]), round(avg_color[1]), round(avg_color[2])))
      #print("new image with filler color")
      #display(newimg)

      newpos = (img.height-img.width)
      newpos = newpos/2
      newimg.paste(img,(int(newpos),0))
      #print("new square image with filler color")
      #display(newimg)
      #newimg = Image.open(newimg)
      return newimg

      #vertically add color
    if img.width > img.height: 
      area = (0, 0, img.width, img.height+ (img.width - img.height))
      cropped_img = img.crop(area)
      newimgsz = [cropped_img.height, cropped_img.width]
    
      newimg = Image.new('RGB', ([newimgsz[1],newimgsz[0]]), (round(avg_color[0]), round(avg_color[1]), round(avg_color[2])))
      #print("new image with filler color")
      #display(newimg)
 
      newpos = (img.width-img.height)
      newpos = newpos/2
      newimg.paste(img,(0,(int(newpos))))
      #print("new square image with filler color")
      #display(newimg)
      #newimg = Image.open(newimg)
      return newimg

# ---- TABS ----
tab1, tab2 = st.tabs(["Demo","Application"])

with tab1:
   st.subheader("Demo")
   
   # Handle first image
   url = "https://raw.githubusercontent.com/webdevserv/images_video/main/cowportrait.jpg" 
   # Handle second image
   url2 = "https://raw.githubusercontent.com/webdevserv/images_video/main/cowlandscape.jpg"

   st.subheader("Square the image")
   img_description = st.text('Image will be squared with color filler where applicable.')

   if st.button('Square and Fill Demo'):  
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.load()

    generated_img = fill_square_image(img)
    st.image(generated_img)

    response = requests.get(url2)
    img = Image.open(BytesIO(response.content))
    img.load()

    generated_img = fill_square_image(img)
    st.image(generated_img)
   

with tab2:
  st.subheader("Square the image")
  img_description = st.text('Image will be squared with color filler where applicable.')
  uploaded_file = st.file_uploader("Upload a JPG image to square and fill with color.", type=['jpg'])

  if uploaded_file is not None: 
   img = Image.open(uploaded_file)
   img.load()
   generated_img = fill_square_image(img)
   st.image(generated_img)
