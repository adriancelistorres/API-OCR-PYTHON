import cv2
import pytesseract

# Cargar la imagen
image = cv2.imread('PRUEBA6.png')

# LO MEJORRRRR PRUEBA 6
# image = cv2.imread('PRUEBA2.png')
# image = cv2.imread('PRUEBA6.png')
# image = cv2.imread('PRUEBA7.png')


# Convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Reemplaza con la ubicación correcta de Tesseract en tu sistema

# Utilizar pytesseract para reconocer texto en la imagen
text = pytesseract.image_to_string(gray)

# Dividir el texto en líneas
lines = text.split('\n')

# Buscar la línea que contiene "servicios"
servicios_line = -1
for i, line in enumerate(lines):
    if "servicios" in line.lower():
        servicios_line = i
        break

# Recortar la parte superior de la imagen hasta la línea de "servicios" y 20 píxeles hacia la izquierda
if servicios_line != -1:
    y_position = servicios_line * 20  # Ajusta la cantidad de píxeles a recortar arriba
    x_position = max(lines[servicios_line].find("Servicios") * 10 - 20, 0)  # Ajusta la cantidad de píxeles a recortar a la izquierda
    image_cropped = image[y_position:, x_position:]
else:
    # Si no se encuentra "servicios," mantener la imagen original
    image_cropped = image



# Guardar la imagen recortada
cv2.imwrite('imagen_recortada.png', image_cropped)
