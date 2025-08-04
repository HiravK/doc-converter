from PIL import Image

def convert_image(input_path, output_path, format):
    img = Image.open(input_path)
    img.save(output_path, format=format.upper())