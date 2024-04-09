from fastapi import FastAPI, UploadFile, File
from PIL import Image
from io import BytesIO
import base64

app = FastAPI()

# Dummy data for demonstration
dummy_text = "Hello, world!"


@app.get("/get_text/")
def get_text(text: str = "Default text"):
    return {"text": text}


@app.post("/process_image/")
def process_image(image_file: UploadFile = File(...)):
    image = Image.open(BytesIO(image_file.file.read()))
    # Process the image here (e.g., resize, apply filters, etc.)
    # For demonstration, we will just return the base64 encoded image
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    encoded_image = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return {"image": encoded_image}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
