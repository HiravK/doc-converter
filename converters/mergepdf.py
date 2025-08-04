from PyPDF2 import PdfFileMerger

def merge_pdfs(pdf_list, output):
    merger = PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output)
    merger.close()