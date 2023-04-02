"""
@author: idoia lerchundi
"""
import openai
import urllib.request
from PIL import Image
import streamlit as st

openai.api_key = "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"

st.set_page_config(
   page_title="Streamlit iCodeIdoia",
   page_icon="images/icon.png",layout="wide",initial_sidebar_state="expanded"
)

st.image("images/banner.jpg")

def generate_image(image_prompt):
 img_response = openai.Image.create(
    prompt = image_prompt,
    n=1,
    size="512x512")    # 256x256, 512x512, 1024x1024

 img_url = img_response['data'][0]['url']

 urllib.request.urlretrieve(img_url, 'image.png')
 #replace cv2 for PIL
 #img = cv2.imread("image.png")
 #cv2_imshow(img)

 img = Image.open("image.png")
 return img

st.subheader('DALL.E - Text-to-Image Generation - OpenAI')

# text input box for image recognition
img_description = st.text_input('Enter image prompt. e.g. hyperrealistic, female web developer coding on a full moon night, back view, wide angle lens')

if st.button('Generate Image'):    
    generated_img = generate_image(img_description)
    st.image(generated_img)