import tempfile
import streamlit as st
from pdf2docx import Converter
from docx2pdf import convert
import os

st.title("📄 Document Converter")

option = st.selectbox("Choose conversion", ["PDF to Word", "Word to PDF"])

uploaded_file = st.file_uploader("Upload your file", type=["pdf", "docx"])

if uploaded_file and st.button("Convert"):
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp:
        tmp.write(uploaded_file.read())
        temp_input_path = tmp.name

    if option == "PDF to Word":
        output = temp_input_path.replace(".pdf", ".docx")
        cv = Converter(temp_input_path)
        cv.convert(output)
        cv.close()
        st.success("Converted to Word.")
        st.download_button("Download Word File", open(output, "rb"), file_name=output)

    elif option == "Word to PDF":
        output = temp_input_path.replace(".docx", ".pdf")
        convert(temp_input_path)
        st.success("Converted to PDF.")
        st.download_button("Download PDF File", open(output, "rb"), file_name=output)

    os.remove(temp_input_path)