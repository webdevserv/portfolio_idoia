
"""
@author: idoia lerchundi
"""

import streamlit.components.v1 as components
import os
from io import BytesIO
from PIL import Image,ImageFile
from rembg import remove


def remove_bg(input_path):
 output_path = 'output/output.png'

 with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        #saves output
        #remove the output file
        saving = o.write(output)

 return output_path


