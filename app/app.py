import streamlit as st
import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt

from src.find_blobs.find_blobs import find_blobs


st.title('Basketball Shot Consistency')

st.markdown("""
Hi, this is an app that helps you determine how consistent your basketball is.

Made with love by Skyler Shi
""")

st.text("")
st.header("Upload Basketball Video First")
vid_upload = st.file_uploader("Upload Bball Video", type = ['mp4'])
st.write(type(vid_upload))
st.video(vid_upload)

if st.button("Run Shot Analysis!"):
    vid_obj = cv2.VideoCapture('../data/shooting_vids/shooting6.mp4')
    fig = plt.figure(1)
    blob_frame = st.empty()
    success = True
    
    while success:
        success, frame = vid_obj.read()
        output = find_blobs(vid_obj, blob_frame).__next__()
        blob_frame.image(output, channels = 'BGR', use_column_width = True)

    # blobs_info, vid_dim = find_blobs(vid_obj, blob_frame)



    

