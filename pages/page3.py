import streamlit as st
from PIL import Image
import pandas as pd
#import matplotlib.pyplot as plt




image = Image.open('./data/スクリーンショット.png')
st.image(image, width=720)

video_file = open('./data/federer.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
