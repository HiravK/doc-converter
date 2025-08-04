import fitz  # PyMuPDF

def compress_pdf(input_path, output_path):
    doc = fitz.open(input_path)
    for page in doc:
        page.compress_content()
    doc.save(output_path, garbage=4, deflate=True)
    