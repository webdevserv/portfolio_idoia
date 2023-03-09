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
SOURCE = "https://raw.githubusercontent.com/webdevserv/images_video/main/cowportrait.jpg"

def create_deepzoom_img(SOURCE):
 
 creator = deepzoom.ImageCreator(
    tile_size=128,
    tile_overlap=2,
    tile_format="png",
    image_quality=0.8,
    resize_filter="bicubic",
 )

 # Create Deep Zoom image pyramid from source
 creator.create(SOURCE, "cowportrait.dzi")

#prefixUrl: "/openseadragon/images/",
#tileSources: "/path/to/my/image.dzi"
#https://openseadragon.github.io/docs/
def view_dzi():
  st.write("1111111111111111111--------------------------")
  #fails https://raw.githubusercontent.com/webdevserv/images_video/main/old/cowportrait_files/0/0_0.png
  components.html("""
  <div id="openseadragon1" style="width: 800px; height: 600px;"></div>
  <script src="https://code.jquery.com/jquery-2.2.4.min.js" integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44=" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.0.0/openseadragon.min.js" crossorigin="anonymous"></script>
  <script type="text/javascript">
    var viewer = OpenSeadragon({
        id: "openseadragon1",
        prefixUrl: "//openseadragon.github.io/openseadragon/images/",
        tileSources: "https://raw.githubusercontent.com/webdevserv/images_video/main/old/cowportrait.dzi"                
    });
   </script> 
   <div id="openseadragon1" style="width: 900px; height: 800px;"></div>
   """,
   height=600,
   )

# Streamlit execution starts in main() function.
def main():     
   
 st.subheader('Deepzoom')
 view_dzi()
 # text input box for image recognition
 img_description = st.text_input('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

 if st.button('Generate deepzoom image'):    
    create_deepzoom_img(SOURCE)
    print("deepzoom image created.")
    #st.image(generated_img)

#st.json({'foo':'bar','fu':'ba'})


components.html(
    """    
    <style>#openseadragon1 {position: fixed;left: 0;top: 0; width: 100%;  height: 100%;}</style>
    <script src="https://code.jquery.com/jquery-2.2.4.min.js" integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44=" crossorigin="anonymous"></script>
    <!--<script src="https://openseadragon.github.io/openseadragon/openseadragon.js"></script>-->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.0.0/openseadragon.min.js"></script>
    <script type="text/javascript">
    // NOTE: this Codepen is for cross-site DZI access (where your code is on one server and your DZI data is on another server) where 
    // you can't set up CORS on the DZI server for whatever reason. That used to be fairly common, but now it's much more rare. 

    // Change this to the path to your "_files" directory on the remote server. 
    //var dziFilesUrl = '//openseadragon.github.io/example-images/duomo/duomo_files/';
    var dziFilesUrl = 'https://raw.githubusercontent.com/webdevserv/images_video/main/old/';

    // Change this to the contents of the .dzi file from your server. 
    var dziData = '<?xml version="1.0" encoding="UTF-8"?><Image xmlns="http://schemas.microsoft.com/deepzoom/2008" TileSize="128" Overlap="2" Format="png"><Size Width="400" Height="533"/></Image>';

    // This converts the XML into a DZI tile source specification object that OpenSeadragon understands. 
    var tileSourceFromData = function(data, filesUrl) {
    var $xml = $($.parseXML(data));
    var $image = $xml.find('Image');
    var $size = $xml.find('Size');

   var dzi = {
     Image: {
       xmlns: $image.attr('xmlns'),
       Url: filesUrl,
       Format: $image.attr('Format'),
       Overlap: $image.attr('Overlap'),
       TileSize: $image.attr('TileSize'),
       Size: {
         Height: $size.attr('Height'),
         Width: $size.attr('Width')
       }
     }
    };  
  
    console.log(dzi);
   return dzi;
 };

 // This creates the actual viewer. 
  var viewer = OpenSeadragon({
   id: 'openseadragon1',
   //prefixUrl: '//openseadragon.github.io/openseadragon/images/',
   //prefixUrl: 'https://raw.githubusercontent.com/webdevserv/images_video/main/old/',
   prefixUrl: 'openseadragon/images/',
   tileSources: 'output/cowportrait.dzi'
   //tileSources: tileSourceFromData(dziData, dziFilesUrl)
  });
 </script>
    <div id="openseadragon1"></div>
    """,
    height=600,
)


#simplified

st.text("---------------------------------------")
#simple
components.html(
    """    
    <style>#openseadragon1 {position: fixed;left: 0;top: 0; width: 100%;  height: 100%;}</style>
    <script src="https://code.jquery.com/jquery-2.2.4.min.js" integrity="sha256-BbhdlvQf/xTY9gja0Dq3HiwQF8LaCRTXxZKRutelT44=" crossorigin="anonymous"></script>
    <!--<script src="https://openseadragon.github.io/openseadragon/openseadragon.js"></script>-->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/openseadragon/4.0.0/openseadragon.min.js"></script>
    <script type="text/javascript">
    // This creates the actual viewer. 
    var viewer = OpenSeadragon({
     id: 'openseadragon1',
     //prefixUrl: '//openseadragon.github.io/openseadragon/images/',
     //prefixUrl: 'https://raw.githubusercontent.com/webdevserv/images_video/main/old/',
     prefixUrl: 'openseadragon/images/',
     tileSources: 'output/cowportrait.dzi'
     //tileSources: tileSourceFromData(dziData, dziFilesUrl)
    });
    </script>
    
   <div id="openseadragon1"></div>
    """,
    height=600,
)














if __name__ == "__main__":
    main()

