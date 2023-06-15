# readme
Web Developer: [Idoia, New York, USA](https://live-webdevserv.pantheonsite.io)

**The content of this page changes as technology evolves**, to keep up to date with changes [follow me on GitHub](https://github.com/webdevserv/portfolio_idoia).

# portfolio_idoia

As ML is an interest of mine, I am creating web apps in streamlit with python code of useful applications. I have an AI degree and I am passionate about web and ML. Django will be also used shortly to deploy some of the models.

There are three web application demonstrated in the repository:

1.- # Super Resolution app

This application demonstrates how SRGAN model can generate a super-resolution image from a low-resolution input.

2.- # Square and Fill appliaton app

This utility takes a landscape image and squares it neatly. It uses a color filler as needed.

3.- # Dall-e image creation showcases from OpenAI

Generates Artificial images using the Dall-e application from OpenAI

File/Folder              | Content

images/.....................images for the app
styles/.....................CSS style sheets
js/.........................javascript
samples/....................useful images for the applications demonstrations
screens/....................screenshots of the application
output/.....................output folder


# Instructions

""" make sure streamlit is uptodate """
pip install streamlit --upgrade

"""go to app folder"""
cd C:\yourpath\portfolio_idoia

""" run the app """
streamlit run iCode*.py
OR
streamlit run id(+tab)

# Served URL

check your terminal window and access the application;
For example:

  Local URL: http://localhost:8501
  Network URL: http://192.168.7.230:8501

# install PIP requirements

pip install -r portfolio_idoia\requirements.txt

# for Dall-e 

pip install openai

# library streamlit-extras 

pip install streamlit-extras  for streamlit-extras library
