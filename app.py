import streamlit as st
st.set_page_config(page_title="Doc Converter", layout="wide")
st.sidebar.title("📁 Doc Converter Tools")
from converters.Batchjpg2pdf import batch_jpg_to_pdf
from pdf_tools.remove_watermark import remove_watermark_tool

def ocr_tool():
    import pytesseract
    from PIL import Image
    import tempfile

    st.header("OCR Tool – Extract Text from Image")
    uploaded_file = st.file_uploader("Upload an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)

        if st.button("Extract Text"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
                img.save(tmp.name)
                text = pytesseract.image_to_string(Image.open(tmp.name))
                st.subheader("Extracted Text:")
                st.text_area("Text", text, height=300)

tool = st.sidebar.selectbox("Choose conversion", [
    "PDF to Word",
    "Word to PDF",
    "JPG to PNG",
    "PNG to JPG",
    "JPG to PDF",
    "Merge PDFs",
    "Compress PDF",
    "Batch JPG to PDF",
    "Remove PDF Watermark",
    "OCR"
])

if tool == "PDF to Word":
    st.header("PDF to Word")
    st.info("Feature coming soon.")

elif tool == "Word to PDF":
    st.header("Word to PDF")
    st.info("Feature coming soon.")

elif tool == "JPG to PNG":
    st.header("JPG to PNG")
    st.info("Feature coming soon.")

elif tool == "PNG to JPG":
    st.header("PNG to JPG")
    st.info("Feature coming soon.")

elif tool == "JPG to PDF":
    st.header("JPG to PDF")
    st.info("Feature coming soon.")

elif tool == "Merge PDFs":
    st.header("Merge PDFs")
    st.info("Feature coming soon.")

elif tool == "Compress PDF":
    st.header("Compress PDF")
    st.info("Feature coming soon.")

elif tool == "Batch JPG to PDF":
    batch_jpg_to_pdf()

elif tool == "Remove PDF Watermark":
    remove_watermark_tool()

elif tool == "OCR":
    ocr_tool()