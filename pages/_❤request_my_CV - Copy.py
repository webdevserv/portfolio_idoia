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
        #st.image(img_contact_form)
        video_file = open('video/metface.mp4', 'rb')
             
        #video_file = open('https://youtube.com/shorts/nQvFCfY_BBc', 'rb')
       
        video_bytes = video_file.read()
        st.video(video_bytes)

        video_html = """
            <video controls="" width="400" height="340" autoplay="true" muted="true" loop="true" anonymous="true">
            <source src="video/metface.mp4" type="video/mp4" />
            <p>
              Your browser doesn't support HTML video. Here is a
              <a href="video/metface.mp4">link to the video</a> instead.</p>
            </video>
        """
        st.markdown(video_html, unsafe_allow_html=True)

        video_html3= """
            <video controls="" src="https://static.streamlit.io/examples/star.mp4" autoplay="true" muted="true" loop="true" class="stVideo" style="width: 400px;"></video>
        """
               
        st.markdown(video_html3, unsafe_allow_html=True)
        
        video_html5= """
            <video controls="" src="video/metface.mp4" autoplay="true" muted="true" loop="true" class="stVideo" style="width: 400px;"></video>
        """
        st.markdown(video_html5, unsafe_allow_html=True)

        video_html4= """
            <video controls="" src="https://youtube.com/shorts/nQvFCfY_BBc" autoplay="true" muted="true" loop="true" class="stVideo" style="width: 400px;"></video>
        """
        st.markdown(video_html4, unsafe_allow_html=True)


with open("video/metface.mp4", 'rb') as v:
    st.video(v)

