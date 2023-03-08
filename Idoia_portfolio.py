import streamlit as st
#from streamlit_lottie import st_lottie
from PIL import Image
import base64
import time

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
   page_title="Stremlit Idoia portfolio App",
   page_icon="😎",layout="wide",initial_sidebar_state="expanded"
)

# left container
#st.sidebar.success("Welcome.")
# my_input=""
# if "my_input" not in st.session_state:
#  st.session_state["my_input"] = ""
# else:
#  my_input = st.text_input("What is your name?", st.session_state["my_input"])
#  submit = st.button("Submit")
#  if submit:
   # st.session_state["my_input"] = my_input
   #st.write("You have entered: ", my_input)

# if len(my_input)> 1:    
   # st.header("Hi there " + my_input+"!")
# else:
   # st.header("Hi there!")
   
st.subheader("Streamlit Idoia Web Portfolio :wave:")
with st.spinner("Loading..."):
        time.sleep(1)

# ---- LOAD ASSETS ----
local_css("style/style.css")
img_anim =  open("images/idoia_working.gif", "rb")
img_flat = Image.open("images/idoia_flat.png")

# ---- HEADER SECTION ----
with st.container():   
 st.write("I am a full stack web developer with international experience (London and New York).")
 st.write("I feel passionate about Web, ML, Data Science. My degree in in Artificial Intelligence. My work experience is on Web front and back end.\
           I enjoy creating web apps with ML models. I find GANs fascinating and also enjoy making videos with latent space interpolations."
    )
 st.write("Learn more Word Press website https://dev-webdevserv.pantheonsite.io/")
 #https://dev-webfrontback.pantheonsite.io/

# ---- TABS ----
tab1, tab2, tab3 = st.tabs(["Projects","Experience","Bio snap"])

with tab1:
   st.subheader("Projects")
   col1, col2 =  st.columns([1,2], gap="small")
with col1:
  #st.image(img_flat)
  youtube_html = """<iframe width="420" height="315" src="https://www.youtube.com/embed/0TCMxuZguY0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; 
clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>"""
  st.markdown(youtube_html, unsafe_allow_html=True)
  #st.write("By (www.idoia.com)")
  st.caption("youtube @WifiNow")
with col2:
  st.write(
 """
I am passionate about ML. Some of the projects I have worked on include:

- Exploring GANs (Generative Adversarial Network) using Google Colab and Jupyter notebooks.
- Building interactive web apps with Python and Streamlit to showcase ML models.
- Developing and deploying ML models with Django framework.
- Creating and styling web apps with Angular and Bootstrap.
  """) 
  
with tab2:
   st.subheader("Experience")
   col1, col2 =  st.columns([1,2], gap="small")

with col1:
   st.image(img_flat)
   #st.write("""By <a href="https://unsplash.com/photos/0g7BJEXq7sU" target="_blank" rel="noopener noreferrer">@phonvanna</a>""")
   st.write("By (www.idoia.com)")

with col2:
   st.write(
  """
  I have worked as a web developer for various companies and agencies in New York and London. Some of the projects I have been involved in are:

  Full stack web development and Word Press theme development using Angular, Bootstrap, WordPress, CSS, HTML, Angular, graphic design. Implemented SEO strategies and created materials for application development for Gamyte.com. ERP Maestro: Maintained and updated web applications using CSS, HTML, JavaScript and C# Visual Studio. Performed troubleshooting and QA tasks.
  Digital Marketing agencies London: Worked as a freelance web developer for several clients such as Diageo, Banking clients and Rio Tinto. Used CSS, HTML, graphics, JavaScript and C# Visual Studio to create and improve web sites/apps.
  iXL: Created custom websites for blue chip clients such as British Airways, Cisco, Dupont, Thistle Hotels, Virgin and UBS. Miller Freeman: Developed a custom project with Pivotal CRM and Formida Floorplanning.
  """) 
   st.write("[Word Press Site >](https://dev-webdevserv.pantheonsite.io/")

with tab3:
   st.subheader("Bio snap")
   col1, col2 = st.columns([1,2], gap="small")

with col1:
  st.image(img_flat)
  #st.write("""By <a href="https://unsplash.com/photos/0g7BJEXq7sU" target="_blank" rel="noopener noreferrer">@phonvanna</a>
  st.write("By (www.idoia.com)")

with col2:
   st.write(
  """
  I have over 25 years of experience in web development. I began my career as a webmaster in 1996 and then joined iXL, a leading interactive agency at the time, as a senior front-end developer. 
There, I created custom websites for prestigious clients such as British Airways, Dupont, UBS, Cisco, Virgin and more. After the dot-com bubble burst, I became a certified MCSD and worked as 
a freelancer using both back end and front end skills.  
  """) 

















