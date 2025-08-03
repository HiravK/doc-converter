import tempfile
import streamlit as st
from pdf2docx import Converter
from docx2pdf import convert
import os
from PIL import Image
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

st.title("📄 Document Converter")

option = st.selectbox("Choose conversion", [
    "PDF to Word",
    "Word to PDF",
    "JPG to PNG",
    "PNG to JPG",
    "JPG to PDF",
    "Merge PDFs",
    "Compress PDF"
])

if option in ["PDF to Word"]:
    file_types = ["pdf"]
elif option == "Word to PDF":
    file_types = ["docx"]
elif option in ["JPG to PNG", "JPG to PDF"]:
    file_types = ["jpg", "jpeg"]
elif option == "PNG to JPG":
    file_types = ["png"]
else:
    file_types = []

uploaded_file = st.file_uploader("Upload your file", type=file_types)

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

    elif option == "JPG to PNG":
        image = Image.open(temp_input_path)
        output = temp_input_path.replace(".jpg", ".png").replace(".jpeg", ".png")
        image.save(output, "PNG")
        st.success("Converted to PNG.")
        st.download_button("Download PNG", open(output, "rb"), file_name=os.path.basename(output))

    elif option == "PNG to JPG":
        image = Image.open(temp_input_path).convert("RGB")
        output = temp_input_path.replace(".png", ".jpg")
        image.save(output, "JPEG")
        st.success("Converted to JPG.")
        st.download_button("Download JPG", open(output, "rb"), file_name=os.path.basename(output))

    elif option == "JPG to PDF":
        image = Image.open(temp_input_path).convert("RGB")
        output = temp_input_path.replace(".jpg", ".pdf").replace(".jpeg", ".pdf")
        image.save(output, "PDF", resolution=100.0)
        st.success("Converted to PDF.")
        st.download_button("Download PDF", open(output, "rb"), file_name=os.path.basename(output))

    os.remove(temp_input_path)

if option == "Merge PDFs":
    uploaded_files = st.file_uploader("Upload PDFs to merge", type=["pdf"], accept_multiple_files=True)
    if uploaded_files and st.button("Merge"):
        merger = PdfMerger()
        for uploaded in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
                tmp_pdf.write(uploaded.read())
                merger.append(tmp_pdf.name)
        output = os.path.join(tempfile.gettempdir(), "merged.pdf")
        merger.write(output)
        merger.close()
        st.success("PDFs merged.")
        st.download_button("Download Merged PDF", open(output, "rb"), file_name="merged.pdf")

if option == "Compress PDF":
    uploaded_file = st.file_uploader("Upload PDF to compress", type=["pdf"])
    if uploaded_file and st.button("Compress"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            temp_input_path = tmp.name

        reader = PdfReader(temp_input_path)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        output = temp_input_path.replace(".pdf", "_compressed.pdf")
        with open(output, "wb") as f:
            writer.write(f)
        st.success("PDF compressed.")
        st.download_button("Download Compressed PDF", open(output, "rb"), file_name=os.path.basename(output))
        os.remove(temp_input_path)