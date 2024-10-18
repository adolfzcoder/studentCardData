import cv2
import pytesseract as tess
from PIL import Image

def get_text_from_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    # Convert the image to RGB (OpenCV uses BGR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Convert the image to PIL format
    image = Image.fromarray(image)
    # Get the text from the image
    text = tess.image_to_string(image)
    # print(text)
    return text