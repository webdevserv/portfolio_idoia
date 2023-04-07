"""
@author: idoia lerchundi
"""
import streamlit as st
from PIL import Image

st.set_page_config(
   layout="wide",
   page_title="Streamlit iCodeIdoia",
   page_icon="images/ilpicon1.png",layout="wide",initial_sidebar_state="expanded"
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.image("images/banner2.jpg")       
st.subheader("Get in touch")

# ---- LOAD ASSETS 
local_css("styles/style.css")
img_working = Image.open("images/idoia_working.gif")
img_art = Image.open("images/add-black-headphones-302253249.png")

with st.container():            
    contact_form = """
    <p>If you're interested in working together or have any questions about my work, please don’t hesitate <a href="https://live-webdevserv.pantheonsite.io/contact/">to get in touch</a>.</p>
    <form action="private007@lineone.net" method="POST">
        <input type="hidden" name="_captcha" value="false" disabled >
        <input type="text" name="name" placeholder="Name" required disabled>
        <input type="text" name="company" placeholder="Company" required disabled>
        <input type="email" name="email" placeholder="Email" required disabled>
        <textarea name="message" placeholder="Message" required disabled></textarea>
        <button type="submit" disabled>Send</button>
    </form>
    """
    left_column, right_column = st.columns([1,2], gap="small")
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        #st.empty()
        st.image(img_art, width=400)   