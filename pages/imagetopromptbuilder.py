import streamlit as st
from PIL import Image

st.set_page_config(
   layout="wide"
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.image("images/banner2.jpg")       
st.subheader("Get in touch")

# ---- LOAD ASSETS ----
local_css("style/style.css")
img_working = Image.open("images/idoia_working.gif")
img_art = Image.open("images/add-black-headphones-302253249.png")

#if (st.session_state) and len(st.session_state["my_input"]) > 0:
 #st.write("You have entered: ", st.session_state["my_input"])

with st.container():            
    contact_form = """
    <form action="youremailaddress" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Email" required>
        <textarea name="message" placeholder="Message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns([1,2], gap="small")
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        #st.empty()
        st.image(img_art, width=400)   