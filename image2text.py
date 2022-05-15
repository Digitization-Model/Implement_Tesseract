import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

image = cv2.imread('imgtest.jpg')

#text = pytesseract.image_to_string(image,lang='spa')
text = pytesseract.image_to_string(image)
print('Texto: ',text)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()