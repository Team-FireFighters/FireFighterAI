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
if st.button('View Latest Satellite View'):
    # Split the screen into two columns
    col1, col2 = st.columns(2)

    # Iterate through the chosen locations and display images in columns
    for index, image in enumerate(chosen_locations):
        if index % 2 == 0:  # Even index, display in col1
            with col1:
                st.image(f'{folder_path}/{image}.png', caption=image, use_column_width=True)
        else:  # Odd index, display in col2
            with col2:
                st.image(f'{folder_path}/{image}.png', caption=image, use_column_width=True)

st.link_button('Detect Fire in Satellite Images', 'http://localhost:5005/')