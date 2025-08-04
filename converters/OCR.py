import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os
import tempfile
import streamlit as st

def run_ocr_tool():
    st.header("OCR (Extract Text)")
    uploaded_file = st.file_uploader("Upload an image or scanned PDF", type=["pdf", "jpg", "jpeg", "png"])
    if uploaded_file and st.button("Extract Text"):
        suffix = os.path.splitext(uploaded_file.name)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            tmp.write(uploaded_file.read())
            path = tmp.name

        if suffix == ".pdf":
            images = convert_from_path(path)
        else:
            images = [Image.open(path)]

        text = ""
        for img in images:
            text += pytesseract.image_to_string(img) + "\n"

        st.text_area("Extracted Text", text, height=300)
        os.remove(path)