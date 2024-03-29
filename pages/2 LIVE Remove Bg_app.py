"""
@author: idoia lerchundi
"""
import streamlit as st
import urllib.request
from io import BytesIO
from PIL import Image,ImageFile
from rembg import remove
from streamlit_component_remove_bg import remove_bg as imported_remove_bg

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

def main():     
   # ---- TABS
   tab1, tab2 = st.tabs(["Demo","Application"])

   with tab1:   
      # Handle first image
      url = 'samples/1.jpg'
      
      st.subheader("Remove background from image demo")
      img_description = st.text('Image background will be removed.')

      if st.button('Remove Background Demo'): 
         st.text("Selected image.")
         sel_image = Image.open(url)
         st.image(sel_image)

         generated_img = imported_remove_bg(sel_image)

         st.text("Image background removed.")      
         st.image(generated_img)  

   with tab2:  
      st.subheader("Remove background from image, place image in samples folder.")

      uploaded_file = st.file_uploader("Upload an image. e.g. Select 1_for_super_resolution.jpg from samples folder.", type=['png', 'jpg', 'jpeg', 'gif'])
      st.caption("Note: this app uses samples folder input path, please change code accordingly.")

      if uploaded_file is not None:
         #PIL            
         lr_image = Image.open(uploaded_file)

         st.text("Your Uploaded Image")
         st.image(lr_image)
         imagepath = "output/output.png"
         inputpath="output/input.png"
         lr_image.save(inputpath)
         
         if st.button('Remove background'):       
            st.text("Please wait a few seconds. Monitor top right of your screen.")            
            imagepath = imagepath + uploaded_file.name
            generated_img = imported_remove_bg(inputpath)
            st.text("Image background removed.")      
            st.image(generated_img)  

if __name__ == "__main__":
    main()