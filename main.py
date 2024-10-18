#import pyautogui as gui
import cv2
import numpy as np
import pytesseract as tess
from PIL import Image
import get_text_from_image as gtfi
# Set the path to the Tesseract executable
tess.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = []
# get text from file
textFromImage = gtfi.get_text_from_image("studentCard1.jpg")

split_data = textFromImage.split('\n')
for line in split_data:
    text.append(line)
    
    
student_number = text[2]
student_name = text[4]
field_of_study = text[7]
qualification_level = text[8]

print(f'Student Number: {student_number} \n Student Name: {student_name} \n Field of Study: {field_of_study} \n Qualification Level: {qualification_level}')
# text.append(textFromImage.strip('\n'))
