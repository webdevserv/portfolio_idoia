import os
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True


streamlit_component_fill_square_cropper101 = components.declare_component(
    name='streamlit_component_fill_square_cropper101',
    path='./streamlit_component_fill_square_cropper101'
)

# To this:
#parent_dir = os.path.dirname(os.path.abspath(__file__))
#build_dir = os.path.join(parent_dir, "frontend/build")
#component = components.declare_component("streamlit_component_fill_square_cropper101", path=build_dir)