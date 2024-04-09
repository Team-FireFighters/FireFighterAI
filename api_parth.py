from fastapi import FastAPI, UploadFile, File
from PIL import Image
from io import BytesIO
import base64
import os
from typing import List

app = FastAPI()

# Dummy data for demonstration
dummy_text = "Hello, world!"


@app.get("/get_text/")
def get_text(text: str = "Default text"):
    return {"text": text}


@app.post("/detect_fire_video")
def process_image(image_file: UploadFile = File(...)):
    image = Image.open(BytesIO(image_file.file.read()))
    # Process the image here (e.g., resize, apply filters, etc.)
    # For demonstration, we will just return the base64 encoded image
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    encoded_image = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return {"image": encoded_image}

@app.post("/get_satellite_images/")
def get_satellite_images(image_names: List[str]):
    images_data = []
    image_names = [i+'.png' for i in image_names]
    for name in image_names:
        image_path = os.path.join('sateliite_fire/India_Forest_Images', name)
        if os.path.exists(image_path):
            with open(image_path, "rb") as f:
                image_data = f.read()
            encoded_image = base64.b64encode(image_data).decode("utf-8")
            images_data.append({"name": name, "image": encoded_image})
        else:
            images_data.append({"name": name, "error": "Image not found"})
    return {"images": images_data}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
