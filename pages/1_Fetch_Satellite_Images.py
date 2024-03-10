import streamlit as st
import os

def get_file_names_without_extension(folder_path):
    file_names = []
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            file_name, file_extension = os.path.splitext(file)
            file_names.append(file_name)
    return file_names

# Example usage:
folder_path = 'sateliite_fire/India_Forest_Images'
locations = get_file_names_without_extension(folder_path)


st.title("Fetch Latest Satellite Images")

chosen_locations = st.multiselect('Choose your location', locations)
if st.button('View Latest satellite View'):
    
    for image in chosen_locations:
        st.image(f'{folder_path}/{image}.png', caption=image, use_column_width=True)