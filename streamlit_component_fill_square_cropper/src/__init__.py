import streamlit.components.v1 as components
#component_zero = components.declare_component(
#    name='fill_square_cropper',
#    path='./streamlit_component_fill_square_cropper'
#)

# To this:
parent_dir = os.path.dirname(os.path.abspath(__file__))
#build_dir = os.path.join(parent_dir, "frontend/build")
component = components.declare_component("fill_square_cropper", path=build_dir)