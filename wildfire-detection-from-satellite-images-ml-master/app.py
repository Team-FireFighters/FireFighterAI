from __future__ import division, print_function
# coding=utf-8
from keras.models import load_model
from keras.preprocessing import image

import sys
import os
import glob
import re
import numpy as np
import random
import ultralytics
# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template, send_file
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
import model
# Define a flask app
app = Flask(__name__)
account_sid = ''
auth_token = ''
# client = Client(account_sid, auth_token)
# Model saved with Keras model.save()
#MODEL_PATH = 'models/classifier.h5'

# Load your trained model
# model = load_model(MODEL_PATH)
# model._make_predict_function()          # Necessary
# print('Model loaded. Start serving...')

# You can also use pretrained model from Keras
# Check https://keras.io/applications/
#from keras.applications.resnet50 import ResNet50
#model = ResNet50(weights='imagenet')
print('Model loaded. Check http://127.0.0.1:5000/')

"""
def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    x = np.expand_dims(x, axis=0)

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
    x = preprocess_input(x, mode='caffe')

    preds = model.predict(x)
    return preds
"""
def get_latest_predict_folder(root_dir):
    predict_folders = [d for d in os.listdir(root_dir) if d.startswith('predict')]
    if not predict_folders:
        return None
    
    # Sort the folders based on creation time
    sorted_folders = sorted(predict_folders, key=lambda x: os.path.getctime(os.path.join(root_dir, x)), reverse=True)
    latest_predict_folder = sorted_folders[0]
    return os.path.join(root_dir, latest_predict_folder)

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        tempr=random.randint(50,101)
        fire = model.predict(file_path)
        if fire:
            if tempr>70: 
                prediction = 'fire'           
            else:
                prediction = 'fire and smoke'
        else:
            prediction = 'no fire'

        return prediction
        # classifier = load_model('classifier.h5')
        # test_image = image.load_img(file_path, target_size = (64, 64))
        # test_image = image.img_to_array(test_image)
        # test_image = np.expand_dims(test_image, axis = 0)
        # result = classifier.predict(test_image)
        # #training_set.class_indices
        # if result[0][0] == 1:
        #     prediction = 'notfire'
        # else:
        #     prediction = 'fire'
        # return prediction 
  
    return None


@app.route('/video', methods=['GET', 'POST'])
def upload_video():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        HOME = "/Users/rishit/Documents/VIT/SEM5_point_5/EPICS"
        ultralytics.checks()
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        os.system(f'cd {HOME}')
        os.system(f'yolo task=detect mode=predict model=/Users/rishit/Documents/VIT/SEM5_point_5/EPICS/best.pt conf=0.25 source={file_path} save=True')
        latest = get_latest_predict_folder('/Users/rishit/Documents/VIT/SEM5_point_5/EPICS/runs/detect')
        return send_file(os.path.join(latest,secure_filename(f.filename)), as_attachment=True)
if __name__ == '__main__':
    # app.run(port=5002, debug=True)

    # Serve the app with gevent
    http_server = WSGIServer(('', 5005), app)
    http_server.serve_forever()
