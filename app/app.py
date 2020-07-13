import streamlit as st
import pandas as pd
import numpy as np


st.title('Basketball Shot Consistency')

st.markdown("""
Hi, this is an app that helps you determine how consistent your basketball is.

Made with love by Skyler Shi
""")

# sidebar stuff
st.sidebar.checkbox('Trace shot')

st.text("")
st.header("Upload Basketball Video First")
vid_upload = st.file_uploader("Upload Bball Video", type = ['mp4'])

if vid_upload is None:
    video_file = open('data/example.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
else:
    st.video(vid_upload)

st.button("Run Shot Analysis!")