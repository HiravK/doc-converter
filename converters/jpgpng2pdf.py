from PIL import Image

def image_to_pdf(input_path, output_path):
    img = Image.open(input_path)
    img.convert("RGB").save(output_path)