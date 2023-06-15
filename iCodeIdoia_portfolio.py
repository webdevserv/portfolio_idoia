"""
@author: idoia lerchundi
"""
from streamlit_extras.buy_me_a_coffee import button
import streamlit as st
from PIL import Image
import time
import streamlit.components.v1 as components

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
   page_title="iCodeIdoia",
   page_icon="images/ilpicon1.png",layout="wide",initial_sidebar_state="expanded"
)
st.image("images/banner.jpg")
st.subheader("iCode Portfolio :wave: via Streamlit")

with st.spinner("Loading..."):
      time.sleep(1)

# ---- LOAD
local_css("styles/style.css")

# ---- HEADER 
with st.container():   
 st.write("Welcome to my iCode portfolio, I am a web developer with international experience (London and New York).")
 st.write("On the left sidebar you will find some of the some applications related to images that I have deployed using Streamlit.")
 link_html="""<p><strong>Web:</strong> learn more about <a href="https://webdevserv.github.io/html_bites/dev/web.html" target="_blank">me</a>.</p>"""
 st.markdown(link_html, unsafe_allow_html=True)

# ---- TABS
tab1, tab2, tab3 = st.tabs(["some projects","more videos","some static HTML/CSS"])
# --- PRELOADS
img_model1 = Image.open("images/modeloutput.jpg")
img_model2 = Image.open("images/modeloutput1.jpg")

with tab1:
   col1, col2 =  st.columns([2,3])
   with col1: 
      st.image(img_model1, width=400)  
      st.caption("AI image detection, Computer Vision (Kaggle). Is it a portrait?")
      link_html="""<p><strong>Kaggle</strong> <a href="https://www.kaggle.com/code/idoial/is-it-a-portrait-1st-model-from-my-data" target="_blank">jupyter notebook code</a>.</p>"""
      st.markdown(link_html, unsafe_allow_html=True)

   with col2:
         st.write(
         """
         ML focus. Some of the projects I have worked on include:
         - Image classification model Kaggle (it it a portrait or a street photo?) FastAI library.
         - Responsive HTML, CSS templates, Figma, Photoshop, Stable Diffusion.
         - GANs (Generative Adversarial Network) using Google Colab and Jupyter notebooks.
         - Building interactive web apps with Python and Streamlit to showcase ML models.
         - Developing and deploying ML models with Django framework.
         - Creating and styling web apps with Angular and Bootstrap.
         - WP child theme creation.
         """)
         button(username="artgen", floating=False, width=221)

with tab2: 
    col1, col2 =  st.columns([2,3])
    with col1:
      vimeo_html = """<a href="https://vimeo.com/413606833" target="_blank">Python app using cv2/dlib library</a> in new window."""
      st.markdown(vimeo_html, unsafe_allow_html=True)
      st.caption("python app using cv2 library")
    
      youtube_html = """<iframe height="400" src="https://youtube.com/embed/fnIzi-2sd3g?feature=share" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"></iframe>"""
      st.markdown(youtube_html, unsafe_allow_html=True)
      st.caption("youtube @WifiNow")
    
      youtube_html = """<iframe width="330" height="350" src="https://www.youtube.com/embed/0TCMxuZguY0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"></iframe>"""
      st.markdown(youtube_html, unsafe_allow_html=True)
      st.caption("youtube @WifiNow")
     
      youtube1_html = """<iframe width="330" height="350" src="https://www.youtube.com/embed/To0OQPaE7II" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"></iframe>"""
      st.markdown(youtube1_html, unsafe_allow_html=True)
      st.caption("youtube @WifiNow")

    with col2:
      intro_html =""" """
      st.markdown(intro_html, unsafe_allow_html=True)

with tab3: 
    col1, col2 =  st.columns([2,3])
    with col1:
      youtube_html = """<iframe width="330" height="820" overflow="hidden!important;" src="https://webdevserv.github.io/html_bites/icecream.html" title="static html" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"></iframe>"""
      st.markdown(youtube_html, unsafe_allow_html=True)
      link_html="""<a href="https://webdevserv.github.io/html_bites/icecream.html" target="_blank">Static HTML site</a> in new window."""
      st.markdown(link_html, unsafe_allow_html=True)

      youtube1_html = """<iframe width="330" height="810" overflow="hidden!important;" src="https://webdevserv.github.io/html_bites/planet.html" title="static html" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"></iframe>"""
      st.markdown(youtube1_html, unsafe_allow_html=True)
      link_html="""<a href="https://webdevserv.github.io/html_bites/planet.html" target="_blank">Static HTML site</a> in new window."""
      st.markdown(link_html, unsafe_allow_html=True)

    with col2:
      intro_html =""" """
      st.markdown(intro_html, unsafe_allow_html=True)          


