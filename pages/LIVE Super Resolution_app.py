"""
 @author: idoia lerchundi
"""
import os
import time
from PIL import Image
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
os.environ["TFHUB_DOWNLOAD_PROGRESS"] = "True"

import streamlit as st
from PIL import Image,ImageFile
import requests
from io import BytesIO
import urllib.request

# Declaring Constants
#IMAGE_PATH = "C:/Users/idoia/Downloads/1.jpg"
#
SAVED_MODEL_PATH = "https://github.com/captain-pool/GSOC/releases/download/1.0.0/esrgan.tar.gz"

st.set_page_config(
   page_title="Streamlit iCodeIdoia",
   page_icon="images/icon.png",layout="wide",initial_sidebar_state="expanded"
)

st.image("images/banner.jpg")

def preprocess_image(image_path):
 """ Loads image from path and preprocesses to make it model ready
      Args:
        image_path: Path to the image file
 """
 #uploaded image displays  but tensorflow requires the full path to be able to handle it, so a hardcode downloads folder path is passed.

 #print("this is what is passed to " + image_path)
 #print(image_path)
 hr_image = tf.image.decode_image(tf.io.read_file(image_path))
  # If PNG, remove the alpha channel. The model only supports
  # images with 3 color channels.
 if hr_image.shape[-1] == 4:
  #print("it is a png file.")
  hr_image = hr_image[...,:-1]
 hr_size = (tf.convert_to_tensor(hr_image.shape[:-1]) // 4) * 4
 hr_image = tf.image.crop_to_bounding_box(hr_image, 0, 0, hr_size[0], hr_size[1])
 hr_image = tf.cast(hr_image, tf.float32)

 return tf.expand_dims(hr_image, 0) 
 
def save_image(image, filename):
  """
    Saves unscaled Tensor Images.
    Args:
      image: 3D image tensor. [height, width, channels]
      filename: Name of the file to save.
  """
  if not isinstance(image, Image.Image):
    image = tf.clip_by_value(image, 0, 255)
    image = Image.fromarray(tf.cast(image, tf.uint8).numpy())
  #image.save("%s.jpg" % filename)
  #print("Saved as %s.jpg" % filename)


def plot_image(image0, title=""):
  """
    Plots images from image tensors.
    Args:
      image: 3D image tensor. [height, width, channels].
      title: Title to display in the plot.
  """
  image1 = np.asarray(image0)
  image2 = tf.clip_by_value(image1, 0, 255)
  image3 = Image.fromarray(tf.cast(image2, tf.uint8).numpy())
  #print(title)
  #print("plot")
  #plt.imshow(image)
  #plt.axis("on")
  #plt.title(title)

  return image3

def downscale_image(image):
  """
      Scales down images using bicubic downsampling.
      Args:
          image: 3D or 4D tensor of preprocessed image
  """
  image_size = []
  if len(image.shape) == 3:
    image_size = [image.shape[1], image.shape[0]]
  else:
    raise ValueError("Dimension mismatch. Can work only on single image.")

  image = tf.squeeze(
      tf.cast(
          tf.clip_by_value(image, 0, 255), tf.uint8))

  lr_image = np.asarray(
    Image.fromarray(image.numpy())
    .resize([image_size[0] // 4, image_size[1] // 4],
              Image.BICUBIC))

  lr_image = tf.expand_dims(lr_image, 0)
  lr_image = tf.cast(lr_image, tf.float32)
  return lr_image

#Performing Super Resolution of images loaded from path
#enhance super resolution gan the image
def esrgan_image(imagename, filenamepath):
 hr_image = preprocess_image(filenamepath)
 title1="Original Image"
 plot_image1 = plot_image(tf.squeeze(hr_image),title="Original")
 #save_image(tf.squeeze(hr_image), filename="Original Image")
 #st.image(plot_image1)

 #model = hub.load("https://tfhub.dev/captain-pool/esrgan-tf2/1")
 model = hub.load("https://github.com/captain-pool/GSOC/releases/download/1.0.0/esrgan.tar.gz")
 start = time.time()
 fake_image = model(hr_image)
 fake_image = tf.squeeze(fake_image)
 st.text("Time Taken: %f" % (time.time() - start))

 # Calculating PSNR wrt Original Image
 # must have 3 channels
 if hr_image.shape[-1] == 4:
  hr_image = hr_image[...,:-1]

 return_image = fake_image
 fake_image = downscale_image(tf.squeeze(fake_image))

 psnr = tf.image.psnr(tf.clip_by_value(fake_image, 0, 255),tf.clip_by_value(hr_image, 0, 255), max_val=255)
 st.text("PSNR Achieved: %f" % psnr)

 # Plotting Super Resolution Image
 plot_image2 = plot_image(tf.squeeze(fake_image),"Super Resolution")
 #save_image(tf.squeeze(fake_image), filename="Super Resolution")
 #st.image(plot_image2)

 return return_image

def main():     
    #ILP
    # Render the readme as markdown using st.markdown.
    #readme_text = st.markdown(get_file_content_as_string("instructions.md"))
    st.sidebar.title("Please select an option")
    app_mode = st.sidebar.selectbox("Choose the app mode",
                                    ["Process Single JPG Image"])
    
    if app_mode == "Process Single JPG Image":
        st.subheader("Enhanced Super Resolution GAN Process Single Image - TensorFlow implementation")
        #readme_text.empty()
        uploaded_file = st.file_uploader("Upload a low resolution JPG image. e.g. Select 1_for_super_resolution.jpg from sample folder.", type=['jpg'])

        if uploaded_file is not None:            
            lr_image = Image.open(uploaded_file)
            st.text("Your Uploaded Image")
            st.image(lr_image)
            time_message="Please wait a few seconds. Look at top right of your screen."
            st.text(time_message)

            if st.button('Generate SR'):                               
                #filename = uploaded_file.name
                #hardcoded upload folder
                filepath = "C:/Users/idoia/OneDrive/CAREER/github/portfolio_idoia/samples/"
                #print("filename " + filename)
                imagepath = filepath + uploaded_file.name
                generated_img = esrgan_image(uploaded_file.name, imagepath)
                st.text("Enhanced Super Resolution GAN image created.")   
                
                st.image(generated_img)  
                
# Download a single file and make its content available as a string.
#@st.cache_data(show_spinner=False)
#def get_file_content_as_string(path):
    #url = 'https://raw.githubusercontent.com/ENGI9805-COMPUTER-VISION/Term-Project/master/' + path
    #response = urllib.request.urlopen(url)
    #return response.read().decode("utf-8")

if __name__ == "__main__":
    main()