import streamlit as st
import os
st.title("Detect Fire in Camera Feed")
HOME = "/Users/rishit/Documents/VIT/SEM5_point_5/EPICS"
import ultralytics
ultralytics.checks()
os.system(f'cd {HOME}')
os.system('!yolo task=detect mode=predict model=/Users/rishit/Documents/VIT/SEM5_point_5/EPICS/best.pt conf=0.25 source=/Users/rishit/Documents/VIT/SEM5_point_5/EPICS/forestfire.mp4 save=True')

# Path to your video file
video_path = "/Users/rishit/Downloads/forestfire.MOV"

# Display video
st.video(video_path)

