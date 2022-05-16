#Liberías necesarias para la ejecución del programa
import cv2
import numpy as np
import pytesseract

#A continuación colocamos la ruta donde tenemos el ejecutable de tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

#Seleccionamos y modificamos la imagen que queremos convertir a texto
#Para que sea leida en python
image = cv2.imread('imgtest.jpg')

#text = pytesseract.image_to_string(image,lang='spa')

#pytesseract.image_to_string selecciona la imagen modificada
#y la convierte a texto
text = pytesseract.image_to_string(image)

#Imprimimos el texto
print('Texto: ',text)

#Mostramos la imagen
cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()