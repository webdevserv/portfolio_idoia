import streamlit as st
from PIL import Image

st.set_page_config(
   layout="wide"
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
st.subheader("Request my CV")

#st.set_page_config(   
   #layout="wide"
#)
# ---- LOAD ASSETS ----
local_css("style/style.css")
img_contact_form = Image.open("images/idoia_working.gif")
img_art = Image.open("images/add-cactus-in-terracotta-pot-845270920.png")
                     
with st.container():        
    if (st.session_state) and len(st.session_state["my_input"]) > 0:
       st.write("Thank you ", st.session_state["my_input"] + " for requesting my CV.")

    contact_form = """
    <form action="idoiapaterson@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Name" required>
        <input type="text" name="company" placeholder="Company" required>
        <input type="email" name="email" placeholder="Email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send request</button>
    </form>
    """
    left_column, right_column = st.columns([1,2], gap="small")
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        #st.empty()
        st.image(img_art, width=400)                                