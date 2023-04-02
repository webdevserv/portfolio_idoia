"""
@author: idoia lerchundi
"""
from PIL import Image,ImageFile
import streamlit as st
from rembg import remove
###
### Change filepath accordingly
###
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
        #display_progress(feedback)

 return output_path

def display_progress(output):
   st.write(output)

def main():     
   # ---- TABS
   tab1, tab2 = st.tabs(["Demo","Application"])

   with tab1:   
      # Handle first image
      #url = "https://raw.githubusercontent.com/webdevserv/images_video/main/1.jpg" 
      url ="C:/Users/idoia/OneDrive/CAREER/github/portfolio_idoia/samples/1.jpg"
      
      st.subheader("Remove background from image demo")
      img_description = st.text('Image background will be removed.')

      if st.button('Remove Background Demo'): 
         st.text("Selected image.")
         sel_image = Image.open(url)
         st.image(sel_image)
         generated_img = remove_bg(url)
         st.text("Image background removed.")        
         
         st.image(generated_img)  

   with tab2:  
      st.subheader("Remove background from image")

      uploaded_file = st.file_uploader("Upload an image. e.g. Select 1_for_super_resolution.jpg from samples folder.", type=['png', 'jpg', 'jpeg', 'gif'])
      st.caption("Note: this app uses samples folder input path, please change code accordingly.")
      if uploaded_file is not None:
         #PIL            
         lr_image = Image.open(uploaded_file)
         st.text("Your Uploaded Image")
         st.image(lr_image)
         st.text("Please wait a few seconds. Monitor top right of your screen.")

         if st.button('Remove background'):                               
            #change the file path to your input directory
            filepath = "C:/Users/idoia/OneDrive/CAREER/github/portfolio_idoia/samples/"
            #print("filepath " + filepath)
            #print("filename " + filename)
            imagepath = filepath + uploaded_file.name
            print(imagepath)
            generated_img = remove_bg(imagepath)
            st.text("Image background removed.")        
            
            st.image(generated_img)  
   
if __name__ == "__main__":
    main()