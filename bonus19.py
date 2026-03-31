import streamlit as st
from PIL import Image

with st.expander('start Camera'):
    # start camera
    camera_image = st.camera_input('Camera')

print(camera_image)

if camera_image:
    #Create Pillow image to gray
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Render the grayscale image on the webpage
    st.image(gray_img)


