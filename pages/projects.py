import streamlit as st
from PIL import Image

st.set_page_config(
   layout="wide"
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.image("images/banner2.jpg")
st.subheader("Projects")

# ---- LOAD ASSETS ----
local_css("style/style.css")
img_port1 = Image.open("images/virgin.png")
img_port2 = Image.open("images/blueyonder.png")
img_port3 = Image.open("images/ba.png")
img_port4 = Image.open("images/erpmaestro.png")
img_port5 = Image.open("images/diageo.png")
img_port6 = Image.open("images/gamyte.png")

with st.container():    
 st.caption("Source: WayBackMachine.org")

 col1, col2, col3 = st.columns([2,2,2], gap="small")
 st.caption("Source: WayBackMachine.org")

 with col1:
   st.write("Virgin Atlantic")
   #st.image("https://static.streamlit.io/examples/cat.jpg", width=150) 
   st.image(img_port1)

   st.write("Virgin Atlantic")
   #st.image("https://static.streamlit.io/examples/cat.jpg", width=150) 
   st.image(img_port2)

 with col2:
   st.write("ERP Maestro")
   #st.image("https://static.streamlit.io/examples/dog.jpg", width=150) 
   st.image(img_port4)

   st.write("Blueyonder")
   #st.image("https://static.streamlit.io/examples/dog.jpg", width=150) 
   st.image(img_port3)

 with col3:
   st.write("British Airways")
   #st.image("https://static.streamlit.io/examples/owl.jpg", width=150) 
   st.image(img_port5)

   st.write("Gamyte")
   #st.image("https://static.streamlit.io/examples/dog.jpg", width=150) 
   st.image(img_port6)