"""
@author: idoia lerchundi
"""
import streamlit as st
from PIL import Image
import time
import streamlit.components.v1 as components

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
   page_title="Streamlit Idoia portfolio App",
   page_icon="images/icon.png",layout="wide",initial_sidebar_state="expanded"
)
st.image("images/banner.jpg")
st.subheader("iCodeIdoia Portfolio :wave: via Streamlit")
with st.spinner("Loading..."):
      time.sleep(1)

# ---- LOAD
local_css("styles/style.css")
#img_anim =  open("images/idoia_working.gif", "rb")
#img_flat = Image.open("images/idoia_flat.png")

# ---- HEADER 
with st.container():   
 st.write("Welcome to my app portfolio, I am a web developer with international experience (London and New York).")
 st.write("On the left sidebar you will find some of the some applications related to images that I have deployed using Streamlit.")
 link_html="""<p><strong>WWW:</strong> learn more about <a href="https://webdevserv.github.io/html_bites/dev/webdev.html" target="_blank">me</a>.</p>"""
 st.markdown(link_html, unsafe_allow_html=True)

# ---- TABS
tab1, tab2, tab3 = st.tabs(["some projects","more videos","some statics html"])

with tab1:
   col1, col2 =  st.columns([1,3])
   with col1: 
      youtube_html = """<iframe height="400" src="https://youtube.com/embed/fnIzi-2sd3g?feature=share" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"></iframe>"""
      st.markdown(youtube_html, unsafe_allow_html=True)
      #st.write("By (www.idoia.com)")
      st.caption("youtube @WifiNow")
   with col2:
         st.write(
         """
         I am passionate about ML. Some of the projects I have worked on include:
         
         - Responsive HTML, CSS templates, Figma, Photoshop, Stable Diffusion.
         - Exploring GANs (Generative Adversarial Network) using Google Colab and Jupyter notebooks.
         - Building interactive web apps with Python and Streamlit to showcase ML models.
         - Developing and deploying ML models with Django framework.
         - Creating and styling web apps with Angular and Bootstrap.
         """) 

with tab2: 
    col1, col2 =  st.columns([2,3])
    with col1:
      youtube_html = """<iframe width="330" height="350" src="https://www.youtube.com/embed/0TCMxuZguY0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"></iframe>"""
      st.markdown(youtube_html, unsafe_allow_html=True)
      #st.write("By (www.idoia.com)")
      st.caption("youtube @WifiNow")
     
      youtube1_html = """<iframe width="330" height="350" src="https://www.youtube.com/embed/To0OQPaE7II" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"></iframe>"""
      st.markdown(youtube1_html, unsafe_allow_html=True)
      #st.write("By (www.idoia.com)")
      st.caption("youtube @WifiNow")

    with col2:
      intro_html =""" """
      st.markdown(intro_html, unsafe_allow_html=True)

with tab3: 
    col1, col2 =  st.columns([2,3])
    with col1:
      youtube_html = """<iframe width="330" height="800" src="https://webdevserv.github.io/html_bites/icecream.html" title="static html" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"></iframe>"""
      st.markdown(youtube_html, unsafe_allow_html=True)
      link_html="""<a href="https://webdevserv.github.io/html_bites/icecream.html" target="_blank">Static HTML site</a> in new window."""
      st.markdown(link_html, unsafe_allow_html=True)

      youtube1_html = """<iframe width="330" height="800" src="https://webdevserv.github.io/html_bites/planet.html" title="static html" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"></iframe>"""
      st.markdown(youtube1_html, unsafe_allow_html=True)
      link_html="""<a href="https://webdevserv.github.io/html_bites/planet.html" target="_blank">Static HTML site</a> in new window."""
      st.markdown(link_html, unsafe_allow_html=True)


    with col2:
      intro_html =""" """
      st.markdown(intro_html, unsafe_allow_html=True)          