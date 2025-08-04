import streamlit as st
from PIL import Image
import os
import tempfile
import atexit

def batch_jpg_to_pdf():
    st.header("Batch JPG to PDF Converter")

    uploaded_files = st.file_uploader(
        "Upload JPG files to convert", 
        type=["jpg", "jpeg"], 
        accept_multiple_files=True
    )

    if uploaded_files and st.button("Convert to PDF"):
        images = []
        for uploaded in uploaded_files:
            try:
                img = Image.open(uploaded).convert("RGB")
                images.append(img)
            except Exception as e:
                st.error(f"Error processing image: {uploaded.name} – {e}")

        if images:
            output_path = os.path.join(tempfile.gettempdir(), "batch_output.pdf")
            images[0].save(output_path, save_all=True, append_images=images[1:])
            st.success("PDF created successfully.")
            with open(output_path, "rb") as f:
                st.download_button("Download PDF", f, file_name="converted.pdf")
            atexit.register(lambda: os.remove(output_path) if os.path.exists(output_path) else None)
        else:
            st.warning("No valid JPG images found.")