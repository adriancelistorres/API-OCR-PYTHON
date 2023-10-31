import cv2
import pytesseract
import numpy as np  # Agrega la importación de NumPy

# Cargar la imagen
image = cv2.imread('PRUEBA3.png')

# Aumentar la resolución de la imagen
scale_percent = 200  # Ajusta este valor según tu necesidad
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
image = cv2.resize(image, (width, height))

# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Eliminación de ruido
image_denoised = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

# Procesamiento de imagen avanzado (puedes añadir más mejoras según sea necesario)
# Ejemplo: enderezar texto, eliminación de sombras, corrección de perspectiva, etc.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Reemplaza con la ubicación correcta de Tesseract en tu sistema

# Mejora de la nitidez
kernel = np.array([[-1, -1, -1],
                   [-1,  9, -1],
                   [-1, -1, -1]])
image_enhanced = cv2.filter2D(image_denoised, -1, kernel)

# Utilizar pytesseract para reconocer texto en la imagen mejorada
text = pytesseract.image_to_string(image_enhanced)

# Guardar la imagen mejorada
cv2.imwrite('imagen_mejorada.png', image_enhanced)

# Realizar acciones con el texto reconocido
# ...

# Imprimir el texto reconocido
print(text)
