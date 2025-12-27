import streamlit as st
from PIL import Image

with st.expander("Start Camera"):

    # start the camera
    camera_image = st.camera_input("camera")

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # render thr grayscale image on the webpage
    st.image(gray_img)
