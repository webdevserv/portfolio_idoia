"""
 @author: idoia lerchundi
 """
import os
import time
from PIL import Image
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
#import matplotlib.pyplot as plt
#import matplotlib
os.environ["TFHUB_DOWNLOAD_PROGRESS"] = "True"

import streamlit as st
from PIL import Image,ImageFile
import requests
from io import BytesIO
import urllib.request

# Declaring Constants
#IMAGE_PATH = "C:/Users/idoia/Downloads/1.jpg"

SAVED_MODEL_PATH = "https://tfhub.dev/captain-pool/esrgan-tf2/1"

st.set_page_config(
   layout="wide"
)

#def preprocess_image(image_path):
def preprocess_image(image_path):
 """ Loads image from path and preprocesses to make it model ready
      Args:
        image_path: Path to the image file
 """
 #uploaded image displays  but tensorflow requires the full path to be able to handle it, so a hardcode downloads folder path is passed.

 #print("this is what is passed to " + image_path)
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
  image.save("%s.jpg" % filename)
  print("Saved as %s.jpg" % filename)

#%matplotlib inline
def plot_image(image, title=""):
  """
    Plots images from image tensors.
    Args:
      image: 3D image tensor. [height, width, channels].
      title: Title to display in the plot.
  """
  image = np.asarray(image)
  image = tf.clip_by_value(image, 0, 255)
  image = Image.fromarray(tf.cast(image, tf.uint8).numpy())

  #plt.imshow(image)
  #plt.axis("off")
  #plt.title(title)
  #image.show()

  return image

#Performing Super Resolution of images loaded from path
#enhance super resolution gan the image
def esrgan_image(imagename, filenamepath):
 hr_image = preprocess_image(filenamepath)
 # Plotting Original Resolution image 
 #plot_image(tf.squeeze(hr_image), title="Original Image")
 #save_image(tf.squeeze(hr_image), filename="Original Image")

 #loads the model
 model = hub.load(SAVED_MODEL_PATH)

 start = time.time()
 fake_image = model(hr_image)
 fake_image = tf.squeeze(fake_image)
 print("Time Taken: %f" % (time.time() - start))

 # Plotting Super Resolution Image
 plot_image1 = plot_image(tf.squeeze(fake_image), title="Super Resolution")
 #removed saving functionality
 #get first part of filename
 #improved_filename = imagename.rsplit('.', 1)
 #not saving
 #save_image(tf.squeeze(fake_image), filename = improved_filename[0]+ "SuperResolutionFile")
 display_time(time.time() - start)
 #time_message2 = "Time taken: %f" % (time.time() - start)
 return plot_image1

def display_time(timeinfo):
   time_info = "Time taken: %f" % (timeinfo)
   st.write(time_info)


# Streamlit execution starts in main() function.
def main():     
    #ILP
    # Render the readme as markdown using st.markdown.
    #readme_text = st.markdown(get_file_content_as_string("instructions.md"))

    # Once we have the dependencies, add a selector for the app mode on the sidebar.
    st.sidebar.title("Please select an option")
    app_mode = st.sidebar.selectbox("Choose the app mode",
                                    ["Process Single JPG Image"])
    
    if app_mode == "Process Single JPG Image":
        st.subheader("Enhanced Super Resolution GAN Process Single Image - TensorFlow implementation")
        #readme_text.empty()
        uploaded_file = st.file_uploader("Upload a low resolution JPG image. e.g. Select 1.jpg from sample folder.", type=['jpg'])

        if uploaded_file is not None:            
            lr_image = Image.open(uploaded_file)
            st.text("Your Uploaded Image")
            st.image(lr_image)
            time_message="Please wait a few seconds. Look at top right of your screen."
            st.text(time_message)

            if st.button('Generate SR'):                               
                #filename = uploaded_file.name
                #hardcoded upload folder
                filepath = "C:/Users/idoia/Downloads/"
                #print("filepath " + filepath)
                #print("filename " + filename)
                imagepath = filepath + uploaded_file.name
                generated_img = esrgan_image(uploaded_file.name, imagepath)
                st.text("Enhanced Super Resolution GAN image created.")
                #st.text("ESRGAN image saved sucessfully, as *SuperResolutionFile.jpg.")              
                
                st.image(generated_img)  
                #if (generated_img):
                  #st.text("Time is "+ time_info)

                                   
# Download a single file and make its content available as a string.
#@st.cache_data(show_spinner=False)
#def get_file_content_as_string(path):
    #url = 'https://raw.githubusercontent.com/ENGI9805-COMPUTER-VISION/Term-Project/master/' + path
    #response = urllib.request.urlopen(url)
    #return response.read().decode("utf-8")

if __name__ == "__main__":
    main()
