import streamlit as st
import os
from PIL import Image
import numpy as np
import scipy as sp
import cv2
from keras.preprocessing import image
from keras.models import load_model
import random
classifier = load_model('./classifier1.h5')

def get_img_array(path):
    img = image.load_img(path)
    return image.img_to_array(img)


def predict_part(inp_arr_image):
    test_image = cv2.resize(inp_arr_image, (64,64))
    test_image = np.expand_dims(test_image, axis = 0)
    result = classifier.predict(test_image)
    #training_set.class_indices
    if result[0][0] == 1:
        prediction = 'notfire'
        return False
    else:
        prediction = 'fire'
        return True


def get_cells_img(np_arr_img, n=64): # considers all n X n grids
    sub_imgs = []
    for row in range((np_arr_img.shape[0]//n)+1):
        for col in range((np_arr_img.shape[1]//n)+1):
            c_0 = col*n
            c_1 = min((c_0+n), np_arr_img.shape[1])
            r_0 = row*n
            r_1 = min((r_0+n), np_arr_img.shape[0])
    #         print(c_0, c_1, " | ", r_0, r_1)
            sub_imgs.append(np_arr_img[r_0:r_1, c_0:c_1,: ])
    return sub_imgs


def predict(img_array):
    
    inp_img = cv2.resize(img_array, (750, 500) )
    fire_pred = [predict_part(img) for img in get_cells_img(inp_img, n=128)]

    fire_cnt = 0
    for p in fire_pred:
        if p:
            fire_cnt += 1
    no_cnt = len(fire_pred) - fire_cnt

    if fire_cnt > 5:
        return True
    else:
        return False




st.title("Detect Fire in Satellite Images")



def get_file_names_without_extension(folder_path):
    file_names = []
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            file_name, file_extension = os.path.splitext(file)
            file_names.append(file_name)
    return file_names


folder_path = 'sateliite_fire/India_Forest_Images'
locations = get_file_names_without_extension(folder_path)


st.title("Fetch Latest Satellite Images")

chosen_locations = st.multiselect('Choose your location', locations)
if st.button('View Latest satellite View'):
    
    for image in chosen_locations:
        st.image(f'{folder_path}/{image}.png', caption=image, use_column_width=True)
        
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
        
    raw_image = Image.open(uploaded_image)
    img_array = image.img_to_array(raw_image)
    tempr=random.randint(50,101)
    fire = predict(img_array)
    if fire:
        if tempr>70: 
            prediction = 'fire'           
        else:
            prediction = 'fire and smoke'
    else:
        prediction = 'no fire'