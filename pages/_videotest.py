import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

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
    left_column, right_column = st.columns([1,1], gap="small")
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:                   
        #needs sizing container
        st.text("1--------------------------")
        video_file = open('video/metface.mp4', 'rb')
        #video_file = open('https://youtube.com/shorts/nQvFCfY_BBc', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)        
       
        st.text("1--------------------------")
        st.text("Autoplay does not work")
        youtube_html = """<iframe width="420" height="315" src="https://www.youtube.com/embed/0TCMxuZguY0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture;web-share" allowfullscreen></iframe>"""
        st.markdown(youtube_html, unsafe_allow_html=True)
        
        st.text("2-----STREALIT documentation coder with streamlit video---------------------") 
        st.text("Autoplay WORLS but ...but....... when using SAME CODE below for local mp4 or global repository it does not work (short or not short video)")
        #streamlit code works but not below see local and central rep path
        video_html3= """
            <video src="https://static.streamlit.io/examples/star.mp4" autoplay="true" muted="true" loop="true" style="width:420px;height:315px"></video>
        """               
        st.markdown(video_html3, unsafe_allow_html=True)
        
        st.text("3--------SAME CODE AS working one above but nothing not working (local mp4)--------")
        #autostart or play does not work, same code as the one working above but local path
        video_html4= """
            <video src="video/metface.mp4" autoplay="true" muted="true" loop="true" style="width:420px;height:315px"></video>
        """
        st.markdown(video_html4, unsafe_allow_html=True)
        
        st.text("4--------SAME CODE AS working one above but nothing not working --------")
        #autostart or paly does not work, same as working code but central repository with HJHDKFHFHKHDHFH path
        video_html5= """
            <video src="https://youtube.com/shorts/nQvFCfY_BBc" autoplay="true" muted="true" loop="true" style="width:420px;height:315px"></video>
        """
        st.markdown(video_html5, unsafe_allow_html=True)


       
       
       
       
