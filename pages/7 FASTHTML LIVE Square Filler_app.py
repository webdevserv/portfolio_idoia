"""
@author: idoia lerchundi
"""
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from PIL import Image
import numpy as np
from io import BytesIO

app = FastAPI()

# Function for cropping and filling the image
def fill_square_cropper(img):
    imgsz = [img.height, img.width]
    avg_color_per_row = np.average(img, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)

    if img.height > img.width:
        newimg = Image.new(
            'RGB',
            (img.height, img.height),
            (round(avg_color[0]), round(avg_color[1]), round(avg_color[2]))
        )
        newpos = (img.height - img.width) // 2
        newimg.paste(img, (newpos, 0))
        return newimg

    elif img.width > img.height:
        newimg = Image.new(
            'RGB',
            (img.width, img.width),
            (round(avg_color[0]), round(avg_color[1]), round(avg_color[2]))
        )
        newpos = (img.width - img.height) // 2
        newimg.paste(img, (0, newpos))
        return newimg
    else:
        return img

@app.get("/", response_class=HTMLResponse)
async def home_page():
    return """
    <html>
    <body>
    <h2>Square and Fill Image App</h2>
    <p>Upload a JPG image to square and fill with color filler.</p>
    <form action="/upload/" enctype="multipart/form-data" method="post">
        <input name="file" type="file">
        <input type="submit">
    </form>
    </body>
    </html>
    """

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    img = Image.open(BytesIO(contents)).convert("RGB")
    squared_img = fill_square_cropper(img)

    # Save the squared image
    output = BytesIO()
    squared_img.save(output, format="JPEG")
    output.seek(0)

    return HTMLResponse(content=f"<h3>Image successfully squared!</h3><img src='data:image/jpeg;base64,{output.getvalue().hex()}' />", media_type="text/html")
