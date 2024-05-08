from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil
from __future__ import division, print_function
# coding=utf-8
from keras.models import load_model
from keras.preprocessing import image

import sys
import os

import numpy as np
import random

# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

import model
from fastapi.responses import JSONResponse

app = FastAPI()

# Define your model prediction function here
def predict_fire(image_path):
    
    temperature = random.randint(50, 101)
    fire_detected = model.predict(image_path)
    if fire_detected:
        if temperature > 70:
            return 'fire'
        else:
            return 'fire and smoke'
    else:
        return 'no fire'

@app.post("/image")
async def process_image(f: UploadFile = File(...)):
    # Save the image temporarily
    file_path = os.path.join('uploads', secure_filename(f.filename))
    with open(file_path, 'wb') as buffer:
        shutil.copyfileobj(f.file, buffer)
    
    # Call your prediction function
    prediction = predict_fire(file_path)
    
    # Delete the temporary image file
    os.remove(file_path)
    
    return JSONResponse(content={"prediction": prediction})

@app.post("/video")
async def process_video(video: UploadFile = File(...)):
    # Process the video here
    # Example: Save the video
    with open("uploaded_video.mp4", "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)
    
    # Return the processed video
    return FileResponse("uploaded_video.mp4")
