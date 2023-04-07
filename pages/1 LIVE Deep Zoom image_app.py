"""
@author: idoia lerchundi
"""
import streamlit as st
import os
#import deepzoom
import streamlit.components.v1 as components

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
   page_title="Streamlit iCodeIdoia",
   page_icon="images/ilpicon1.png",layout="wide",initial_sidebar_state="expanded"
)

# ---- LOAD
local_css("styles/style.css")
st.image("images/banner.jpg")

# Specify your source image
#SOURCE = "https://raw.githubusercontent.com/webdevserv/images_video/main/ref/imgsrc/playa.jpg"
SOURCE = "https://raw.githubusercontent.com/webdevserv/images_video/main/ref/imgsrc/societa.jpg"
#creator of *.dzi Microsoft deep zoom image

def create_deepzoom_img(SOURCE): 
 creator = deepzoom.ImageCreator(
    tile_size=254,
    tile_overlap=1,
    tile_format="jpg",
    image_quality=0.9,
    resize_filter="bicubic"        
 )
 creator.create(SOURCE, "images/societa.dzi")

def view_versalles():
  #move dzi and pyramid folder to central rep
  components.html("""
  <div id="openseadragon1" style="width: 800px; height: 600px;"></div>
  <script src="https://code.jquery.com/jquery-2.2.4.min.js" integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44=" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.0.0/openseadragon.min.js" crossorigin="anonymous"></script>
  <script type="text/javascript">
    var viewer = OpenSeadragon({
        id: "openseadragon1",
        prefixUrl: "//openseadragon.github.io/openseadragon/images/",
        tileSources: "https://raw.githubusercontent.com/webdevserv/images_video/main/ref/versalles.dzi"                
    });
   </script> 
   """,
   height=600,
   )

def view_ladies():
  #move dzi and pyramid folder to central rep
  components.html("""
  <div id="openseadragon1" style="width: 800px; height: 600px;"></div>
  <script src="https://code.jquery.com/jquery-2.2.4.min.js" integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44=" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.0.0/openseadragon.min.js" crossorigin="anonymous"></script>
  <script type="text/javascript">
    var viewer = OpenSeadragon({
        id: "openseadragon1",
        prefixUrl: "//openseadragon.github.io/openseadragon/images/",
        tileSources: "https://raw.githubusercontent.com/webdevserv/images_video/main/ref/ontario.dzi"                
    });
   </script> 
   <div id="openseadragon1" style="width: 800px; height: 600px;"></div>
   """,
   height=600,
   )
  
def view_societa():
   #move dzi and pyramid folder to central rep
   components.html("""
   <div id="openseadragon1" style="width: 800px; height: 600px;"></div>
   <script src="https://code.jquery.com/jquery-2.2.4.min.js" integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44=" crossorigin="anonymous"></script>
   <script src="https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.0.0/openseadragon.min.js" crossorigin="anonymous"></script>
   <script type="text/javascript">
      var viewer = OpenSeadragon({
         id: "openseadragon1",
         prefixUrl: "//openseadragon.github.io/openseadragon/images/",
         tileSources: "https://raw.githubusercontent.com/webdevserv/images_video/main/ref/societa.dzi"                
      });
      </script> 
      """,
      height=600,
   )

#viewer of *.dzi deep zoom image
def view_dzi():
  components.html("""
   <div id="main-viewer">
    <div id="nav-viewer">
        <div class="selection"></div>
    </div>
  </div>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.3/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.0.0/openseadragon.min.js" crossorigin="anonymous"></script>
  <style>
   #main-viewer {
      position: relative;
      width: 800px;
      height: 600px;
   }

   #nav-viewer {
      position: absolute;
      width: 200px;
      height: 150px;
      right: 0;
      bottom: 0;
      z-index: 10;
      background: black;
      overflow: hidden;
   }

   .selection {
      position: absolute;
      border: 1px solid red;
      z-index: 20;
   }  
  </style>
  <script type="text/javascript">
   var cowportrait = {
   Image: {
      xmlns: 'http://schemas.microsoft.com/deepzoom/2008',
      Url: '//openseadragon.github.io/example-images/duomo/duomo_files/',
      Format: 'jpg',
      Overlap: '2',
      TileSize: '256',
      Size: {
         Width:  '13920',
         Height: '10200'
      }
   }
   }; 
  
   var viewer = OpenSeadragon({
   id: 'main-viewer',
   prefixUrl: '//openseadragon.github.io/openseadragon/images/',
   tileSources: cowportrait,
   showNavigator: true
   });

   var navViewer = OpenSeadragon({
   id: 'nav-viewer',
   prefixUrl: '//openseadragon.github.io/openseadragon/images/',
   tileSources: cowportrait,
   mouseNavEnabled: false,
   showNavigationControl: false,
   });
      
   function updateSelection() {
   var homeBounds = viewer.viewport.getHomeBounds();
   var viewportBounds = viewer.viewport.getBounds(true);
   var $selection = $('.selection');
   var $nav = $('#nav-viewer');
   var navWidth = $nav.width();
   var navHeight = $nav.height();
   var scale = navWidth / homeBounds.width;

   $selection.css({
      left: (viewportBounds.x - homeBounds.x) * scale,
      top: (viewportBounds.y - homeBounds.y) * scale,
      width: viewportBounds.width * scale,
      height: viewportBounds.height * scale
   });
   }

   viewer.addHandler('open', updateSelection);
   viewer.addHandler('animation', updateSelection);
</script>  
   """,
   height=600,
   )
  
#tileSources:
# Streamlit execution starts in main() function.
def main():      
# ---- TABS ----
 tab1, tab2, tab3, tab4 = st.tabs(["Versalles viewer","Cannery viewer","Societa in Sorrento viewer", "Create deepzoom image (.dzi)"])
 with tab1:   
  # Handle first image
  #url = "https://raw.githubusercontent.com/webdevserv/images_video/main/cowportrait.jpg" 
     
  st.subheader("OpenSeaDragon deepzoom viewer")
  img_description = st.text('Instructions: Top small window, move around the slide by dragging, and use the mouse wheel to zoom.')
  view_versalles()
  #view_dzi()
  #eskuz; change dzi content to "Format":"jpg","Overlap":"2",TileSize":"256","Size":{"Height": "9221","Width":"7026"}
  st.caption("Special thanks for openseadragon viewer; @github.com/openseadragon")
  st.caption("Photograph, Chris Bertram, Versailles, @flickr.")
  
 with tab2:
  st.subheader("OpenSeaDragon deepzoom viewer")
  img_description = st.text('Instructions: Move around the slide by dragging, and use the mouse wheel to zoom.')
  view_ladies()
  #eskuz; change dzi content to "Format":"jpg","Overlap":"2",TileSize":"256","Size":{"Height": "9221","Width":"7026"}
  st.caption("Special thanks for openseadragon viewer; @github.com/openseadragon")
  st.caption("Photograph, Deseronto Archives. 1930 Cannery, Ontario, Canada, @flickr.")
  
 with tab3:
  st.subheader("OpenSeaDragon deepzoom viewer")
  img_description = st.text('Instructions: Move around the slide by dragging, and use the mouse wheel to zoom.')
  view_societa()
  #eskuz; change dzi content to "Format":"jpg","Overlap":"2",TileSize":"256","Size":{"Height": "9221","Width":"7026"}
  st.caption("Special thanks for openseadragon viewer; @github.com/openseadragon")
  st.caption("Photograph, Ronel Reyes, Sorrento, @flickr.")
  
 with tab4:
  st.subheader("Deepzoom image creator (dzi)")
  #img_description = st.text('xxxxx.')
  #uploaded_file = st.file_uploader("Upload an image convert into Microsoft deep zoom image *.dzi", type=['jpg','png']
  st.write("For internal use only.")
  #see source file at beginning of file
  #Source file: https://raw.githubusercontent.com/yourrepository/main/yourimage.jpg")     
  #st.write("Output folder is images/dzi") 
  #st.caption("Special thanks for deepzoom library; OpenZoom <http://openzoom.org/>, Daniel Gasienica <daniel@gasienica.ch>, Kapil Thangavelu <kapil.foss@gmail.com>")

if __name__ == "__main__":
   main()