import cv2
import pytesseract

# Cargamos la imagen
imagen = cv2.imread('PRUEBA2.png')

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Reemplaza con la ubicación correcta de Tesseract en tu sistema

# Utilizamos Tesseract para reconocer el texto en la imagen
texto = pytesseract.image_to_string(imagen)

# Buscamos la posición de la palabra "Servicios" en el texto reconocido
posicion_servicios = texto.find("Servicios")

# Si se encuentra la palabra "Servicios" en el texto
if posicion_servicios != -1:
    # Define las coordenadas de corte a partir de la posición de "Servicios"
    corte_izquierda = 60
    corte_arriba = 0
    corte_derecha = imagen.shape[1]   # Usamos la posición de "Servicios" como límite derecho
    corte_abajo = imagen.shape[0]  # Alto de la imagen completa
    
    # Realiza el recorte de la imagen con las coordenadas especificadas
    imagen_recortada = imagen[corte_arriba:corte_abajo, corte_izquierda:corte_derecha]

    # Guarda la nueva imagen recortada
    cv2.imwrite('imagen_recortada_izquierda.png', imagen_recortada)
else:
    print("La palabra 'Servicios' no se encontró en la imagen.")
