#!/usr/bin/env python3
import streamlit as st
import os
import deepzoom
import streamlit.components.v1 as components

st.set_page_config(
   page_title="Streamlit iCodeIdoia",
   page_icon="images/icon.png",layout="wide",initial_sidebar_state="expanded"
)

st.image("images/banner.jpg")

# Specify your source image
#SOURCE = "https://raw.githubusercontent.com/webdevserv/images_video/main/cowportrait.jpg"

#SOURCE = "https://raw.githubusercontent.com/webdevserv/images_video//main/old/test.png"
SOURCE = "https://raw.githubusercontent.com/webdevserv/images_video//main/old/837168218_right.png"

#creator of *.dzi Microsoft deep zoom image
def create_deepzoom_img(SOURCE): 
 creator = deepzoom.ImageCreator(
    tile_size=254,
    tile_overlap=1,
    tile_format="jpg",
    image_quality=0.8,
    resize_filter="bicubic"        
 )
 # Create Deep Zoom image pyramid from source
 # if not a single filename it does not save the slices

 ###########See if it can create it in images/dzi
 creator.create(SOURCE, "bad.dzi")

#https://openseadragon.github.io/docs/

#viewer of *.dzi deep zoom image
def view_cow():
  components.html("""
  <div id="openseadragon1" style="width: 800px; height: 600px;"></div>
  <script src="https://code.jquery.com/jquery-2.2.4.min.js" integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44=" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.0.0/openseadragon.min.js" crossorigin="anonymous"></script>
  <script type="text/javascript">
    var viewer = OpenSeadragon({
        id: "openseadragon1",
        prefixUrl: "//openseadragon.github.io/openseadragon/images/",
        tileSources: "https://raw.githubusercontent.com/webdevserv/images_video/main/old/bad.dzi"                
    });
   </script> 
   <div id="openseadragon1" style="width: 800px; height: 600px;"></div>
   """,
   height=600,
   )

# Streamlit execution starts in main() function.
def main():      
# ---- TABS ----
 tab1, tab2 = st.tabs(["OpenSeaDragon deepzoom viewer","Create deepzoom image (.dzi)"])
 with tab1:   
  # Handle first image
  #url = "https://raw.githubusercontent.com/webdevserv/images_video/main/cowportrait.jpg" 
     
  st.subheader("OpenSeadDragon deepzoom viewer")
  img_description = st.text('Instructions: Move around the slide by dragging, and use the mouse wheel to zoom.')
  view_cow()
  #eskuz; change dzi content to "Format":"jpg","Overlap":"2",TileSize":"256","Size":{"Height": "9221","Width":"7026"}
  st.caption("Special thanks for openseadragon viewer; https://github.com/openseadragon")
  
 with tab2:
  st.subheader("Deepzoom image creator")
 #img_description = st.text('xxxxx.')
 #uploaded_file = st.file_uploader("Upload an image convert into Microsoft deep zoom image *.dzi", type=['jpg','png']
  st.write("Source file: https://raw.githubusercontent.com/webdevserv/images_video/main/cowportrait.jpg")     

 if st.button('Generate deepzoom image'):    
  create_deepzoom_img(SOURCE)
  st.write("Deepzoom *.dzi image created in images/dzi.")
  
 st.caption("Special thanks for deepzoom library; OpenZoom <http://openzoom.org/>, Daniel Gasienica <daniel@gasienica.ch>, Kapil Thangavelu <kapil.foss@gmail.com>")

if __name__ == "__main__":
   main()