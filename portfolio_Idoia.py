import requests
import streamlit as st
#from streamlit_lottie import st_lottie
from PIL import Image

my_input=""

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
   page_title="Stremlit Portfolio App",
   page_icon="😎",layout="wide"
)

st.subheader("Idoia Portfolio")
st.sidebar.success("Welcome.")

if "my_input" not in st.session_state:
 st.session_state["my_input"] = ""
else:
 my_input = st.text_input("What is your name?", st.session_state["my_input"])
 submit = st.button("Submit")

 if submit:
   st.session_state["my_input"] = my_input
   #st.write("You have entered: ", my_input)

# ---- LOAD ASSETS ----
local_css("style/style.css")
img_contact_form = Image.open("images/idoia_working.gif")

# ---- HEADER SECTION ----
with st.container():   
 if len(my_input)> 1:    
    st.header("Hi there " + my_input+"!")
 else:
    st.header("Hi there!")

 st.subheader("My name is Idoia, phonetically easy, try with me. I D O I A. :wave:")
 st.write("I am a full stack web developer with international experience (London and New York).")
 st.write(
        "I am passionate about Web, ML, Data Science. I have an AI degree and I have always worked in Web front and back end. I like creating web apps with ML models. I find GANs fascinating and also enjoy making videos with latent space interpolations."
    )
 st.write("Learn More https://xxxxxxx.com")

# ---- TABS ----
tab1, tab2, tab3 = st.tabs(["Interests", "Experience", "Projects"])

with tab1:
   st.subheader("Interests")
   col1, col2 = st.columns([1,5], gap="small")

with col1:
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
   #st.write("""By <a href="https://unsplash.com/photos/0g7BJEXq7sU" target="_blank" rel="noopener noreferrer">@phonvanna</a>""")
   st.write("By (www.idoia.com)")

with col2:
   st.write(
  """
  My interests in my ML journey are:
  - exploring GANs (Generative Adversarial Network) running in google colab notebooks and Jupyter notebooks.
  - creating ML related Web Apps out from Python google colab notebooks.
  - deploying ML models with Streamlit.
  - deploying ML models with Django.
  - Angular framework and styling web apps with Bootstrap.              
   """) 
   st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")


with tab2:
   st.subheader("Experience")
   col1, col2 = st.columns([1,5], gap="small")

with col1:
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
   #st.write("""By <a href="https://unsplash.com/photos/0g7BJEXq7sU" target="_blank" rel="noopener noreferrer">@phonvanna</a>
   st.write("By (www.idoia.com)")

with col2:
   st.write(
  """
  My interests in my ML journey are:
  - exploring GANs (Generative Adversarial Network) running in google colab notebooks and Jupyter notebooks.
  - creating ML related Web Apps out from Python google colab notebooks.
  - deploying ML models with Streamlit.
  - deploying ML models with Django.
  - Angular framework and styling web apps with Bootstrap.              
   """) 
   st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")

with tab3:
   st.subheader("Projects")
   col1, col2 = st.columns([1,5], gap="small")
with col1:
  st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
  #st.write("""By <a href="https://unsplash.com/photos/0g7BJEXq7sU" target="_blank" rel="noopener noreferrer">@phonvanna</a>
  st.write("By (www.idoia.com)")
with col2:
  st.write(
 """
 My interests in my ML journey are:
 - exploring GANs (Generative Adversarial Network) running in google colab notebooks and Jupyter notebooks.
 - creating ML related Web Apps out from Python google colab notebooks.
 - deploying ML models with Streamlit.
 - deploying ML models with Django.
 - Angular framework and styling web apps with Bootstrap.              
  """) 
  st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my YouTube channel I am creating videos on ML journey:
            - exploring GANs (Generative Adversarial Network) running in google colab notebooks and Jupyter notebooks.
            - creating ML related Web Apps out from Python google colab notebooks.
            - deploying ML models with Streamlit.
            - deploying ML models with Django.
            - Angular framework and styling web apps with Bootstrap.              
             """
        )                     
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        #st_lottie(lottie_coding, height=300, key="coding")
        video_file = open('video/idoiaillustration.mp4', 'rb')
        video_bytes = video_file.read()

        st.video(video_bytes)

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Integrate Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
            In this tutorial, I'll show you exactly how to do it
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("How To Add A Contact Form To Your Streamlit App")
        st.write(
            """
            Want to add a contact form to your Streamlit website?
            In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get in touch.")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
