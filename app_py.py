import streamlit as st
import keras
from PIL import Image, ImageOps
st.title("Klasifikasi Bumbu Dapur")
st.header("Kencur| Jahe| Lengkuas| Kunyit")
st.text("Upload Gambar")

from img_klasifikasi_bumbu import bumbu_dapur

uploaded_file = st.file_uploader("Masukan Gambar...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Gambar Bumbu.', use_column_width=True)
    st.write("")
    st.write("Klasifikasi...")
    label = bumbu_dapur(image, 'keras_model.h5')
    if label == 0:
        st.write("jahe")
    if label == 1:
        st.write("kencur")
    if label == 2:
        st.write("kunyit")
    if label == 3:
        st.write("Lengkuas")