import streamlit as st
from PIL import Image, ImageFilter
import os

# create a folder images
if not os.path.exists('images'):
    os.makedirs('images')

def save_image(image):
    img = Image.open(image)
    img.save(f'images/{image.name}.png')

st.title('🖼️ Image Processing App')

upload = st.file_uploader(
    label='Upload your image',
    type=['png', 'jpg', 'jpeg']
)
if upload is not None:
    save_image(upload)
    img = Image.open(upload)
    col1, col2 = st.columns(2)

    filters = ['contour','emboss','edge_enhance','blur','smooth','sharpen']
    option = st.sidebar.selectbox( 'Select a filter',filters)
    col1.image( upload,  caption='Uploaded Image', use_column_width=True)
    if option == 'contour':
        col2.image(img.filter(ImageFilter.CONTOUR),  caption='Contour Filter',  use_column_width=True)
    if option == 'emboss':
        col2.image(img.filter(ImageFilter.EMBOSS),  caption='Emboss Filter',  use_column_width=True)
