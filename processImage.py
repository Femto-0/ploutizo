from PIL import Image
import pytesseract


def extarct_text_from_image(image_path):
    image = Image.open('image_path')
    return pytesseract.imae_to_string(image)
