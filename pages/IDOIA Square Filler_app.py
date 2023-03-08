"""
@author: idoia lerchundi
"""
import urllib.request
from PIL import Image,ImageFile
import streamlit as st
import numpy as np
import requests
from io import BytesIO

#import os
color=(0,0,255)

#warps does not use filler color
def fill_square_image(img):
    imgsz = [img.height, img.width]

    original_size = imgsz
    print("original image")
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
      print("area is")
      print(area)
      newimgsz = [cropped_img.height, cropped_img.width]
    
      #round(avg_color)
      print("round avg_color")
      print(round(avg_color[0]))
      newimg = Image.new('RGB', ([newimgsz[1],newimgsz[0]]), (round(avg_color[0]), round(avg_color[1]), round(avg_color[2])))
      #print("new image with filler color")
      #display(newimg)

      newpos = (img.height-img.width)
      newpos = newpos/2
      newimg.paste(img,(int(newpos),0))
      print("new square image with filler color")
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
      print("new square image with filler color")
      #display(newimg)
      #newimg = Image.open(newimg)
      return newimg


# Handle first image
url = "https://github.com/webdevserv/portfolio_idoia/blob/main/images/cowportrait.jpg"
# Handle second image
url2 = "https://github.com/webdevserv/portfolio_idoia/blob/main/images/cowlandsscape.jpg"

st.title('Square image and use color Filler if needed')

# text input box for image recognition
img_description = st.text('Image will be squared with color filler if applicable.')

if st.button('Square and Fill'):  
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
   
    