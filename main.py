import streamlit as st
from PIL import Image, ImageFilter
from io import BytesIO

st.set_page_config(layout="wide", page_title="Sketch Creator")

st.write("## Make a sketch from your photo")
st.write("Upload an image to convert it to a sketch."
)
slider_input = st.slider('Set threshold', 0, 255, 100, key='my_slider')
st.sidebar.write("## Upload and download")

def get_sketch(img):
    img_gray = img.convert("L")
    threshold = st.session_state.my_slider
    img_th = img_gray.point(lambda x: 255 if x > threshold else 0)
    return img_th.filter(ImageFilter.CONTOUR)
    # return img_th.filter(ImageFilter.EDGE_ENHANCE)

def fix_image(uploaded_image):
    image = Image.open(uploaded_image)
    col1.write("Photo")
    col1.image(image)

    fixed = get_sketch(image)
    col2.write("Sketch")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    #st.sidebar.download_button("Download fixed image", convert_image(fixed), "fixed.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], 
                                     accept_multiple_files=False)

if my_upload is not None:
    fix_image(uploaded_image=my_upload)
else:
    fix_image("./zebra.png")