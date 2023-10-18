from PIL import Image
import pytesseract
from flask import Flask, request, jsonify
import base64
import io

app = Flask(__name__)

@app.route('/realizar-ocr', methods=['POST'])
def realizar_ocr():
    try:
        # Obtener la imagen base64 desde la solicitud
        data = request.json
        imagen_base64 = data['imagen_base64']

        # Decodificar la imagen base64
        imagen_bytes = base64.b64decode(imagen_base64)

        # Crear una imagen PIL desde los bytes decodificados
        imagen_original = Image.open(io.BytesIO(imagen_bytes))

      # Realizar el recorte de la imagen en partes más pequeñas
        # Define las coordenadas de recorte según tus necesidades
        coordenadas_corte1 = (0, 0, 250, 100)
        parte_cortada1 = imagen_original.crop(coordenadas_corte1)

        # Define las coordenadas para cortar la segunda parte de la imagen (a la derecha de la primera)
        coordenadas_corte2 = (coordenadas_corte1[2], 0, coordenadas_corte1[2] + 250, 100)
        parte_cortada2 = imagen_original.crop(coordenadas_corte2)

        # Define las coordenadas para cortar la tercera parte de la imagen (a la derecha de la segunda)
        coordenadas_corte3 = (coordenadas_corte2[2], 0, coordenadas_corte2[2] + 300, 100)
        parte_cortada3 = imagen_original.crop(coordenadas_corte3)

        # Define las coordenadas para cortar la tercera parte de la imagen (a la derecha de la segunda)
        coordenadas_corte4 = (coordenadas_corte3[2], 0, coordenadas_corte3[2] + 300, 100)
        parte_cortada4 = imagen_original.crop(coordenadas_corte4)

        # Define las coordenadas para cortar la quinta parte de la imagen (abajo de la primera)
        coordenadas_corte5 = (0, coordenadas_corte1[3], 300, coordenadas_corte1[3] + 60)  # Ajusta estas coordenadas para la quinta parte

        # Corta la quinta parte deseada de la imagen original
        parte_cortada5 = imagen_original.crop(coordenadas_corte5)

        # Define las coordenadas para cortar la sexta parte de la imagen (al costado del corte 5)
        coordenadas_corte6 = (coordenadas_corte5[2], coordenadas_corte1[3], coordenadas_corte5[2] + 150, coordenadas_corte1[3] + 60)  # Ajusta estas coordenadas para la sexta parte

        # Corta la sexta parte deseada de la imagen original
        parte_cortada6 = imagen_original.crop(coordenadas_corte6)

        # Define las coordenadas para cortar la séptima parte de la imagen (al costado del corte 6)
        coordenadas_corte7 = (coordenadas_corte6[2], coordenadas_corte6[1], coordenadas_corte6[2] + 400, coordenadas_corte6[3])  # Ajusta estas coordenadas para la séptima parte

        # Corta la séptima parte deseada de la imagen original
        parte_cortada7 = imagen_original.crop(coordenadas_corte7)

        # Define las coordenadas para cortar la octava parte de la imagen (debajo del corte 5)
        coordenadas_corte8 = (0, coordenadas_corte5[3], 300, coordenadas_corte5[3] + 100)  # Ajusta estas coordenadas para la octava parte

        # Corta la octava parte deseada de la imagen original
        parte_cortada8 = imagen_original.crop(coordenadas_corte8)

        # Define las coordenadas para cortar la novena parte de la imagen (al costado del corte 8)
        coordenadas_corte9 = (coordenadas_corte8[2], coordenadas_corte8[1], coordenadas_corte8[2] + 250, coordenadas_corte8[3])  # Ajusta estas coordenadas para la novena parte

        # Corta la novena parte deseada de la imagen original
        parte_cortada9 = imagen_original.crop(coordenadas_corte9)

        # Define las coordenadas para cortar la novena parte de la imagen (al costado del corte 8)
        coordenadas_corte10 = (coordenadas_corte9[2], coordenadas_corte9[1], coordenadas_corte9[2] + 350, coordenadas_corte9[3])  # Ajusta estas coordenadas para la novena parte

        # Corta la novena parte deseada de la imagen original
        parte_cortada10 = imagen_original.crop(coordenadas_corte10)

        # Define las coordenadas para cortar la novena parte de la imagen (al costado del corte 8)
        coordenadas_corte11 = (coordenadas_corte10[2], coordenadas_corte10[1], coordenadas_corte10[2] + 350, coordenadas_corte10[3])  # Ajusta estas coordenadas para la novena parte

        # Corta la novena parte deseada de la imagen original
        parte_cortada11 = imagen_original.crop(coordenadas_corte11)

        nuevo_ancho, nuevo_alto = parte_cortada1.size


        # Crea una lista para almacenar el texto de cada imagen
        texto_imagenes = []

        nuevo_ancho, nuevo_alto = parte_cortada1.size


        pytesseract.pytesseract.tesseract_cmd = r'C:\ROM_Projects\API-OCR\API-OCR-PYTHON\Tesseract-OCR\tesseract.exe'  # Reemplaza con la ubicación correcta de Tesseract en tu sistema

        # Aplica OCR para obtener el texto de cada imagen
        texto_imagen1 = pytesseract.image_to_string(parte_cortada1)
        texto_imagen2 = pytesseract.image_to_string(parte_cortada2)
        texto_imagen3 = pytesseract.image_to_string(parte_cortada3)
        texto_imagen4 = pytesseract.image_to_string(parte_cortada4)
        texto_imagen5 = pytesseract.image_to_string(parte_cortada5)
        texto_imagen6 = pytesseract.image_to_string(parte_cortada6)
        texto_imagen7 = pytesseract.image_to_string(parte_cortada7)
        texto_imagen8 = pytesseract.image_to_string(parte_cortada8)
        texto_imagen9 = pytesseract.image_to_string(parte_cortada9)
        texto_imagen10 = pytesseract.image_to_string(parte_cortada10)
        texto_imagen11 = pytesseract.image_to_string(parte_cortada11)

        # Agrega el texto de cada imagen a la lista
        texto_imagenes.append(texto_imagen1)
        texto_imagenes.append(texto_imagen2)
        texto_imagenes.append(texto_imagen3)
        texto_imagenes.append(texto_imagen4)
        texto_imagenes.append(texto_imagen5)
        texto_imagenes.append(texto_imagen6)
        texto_imagenes.append(texto_imagen7)
        texto_imagenes.append(texto_imagen8)
        texto_imagenes.append(texto_imagen9)
        texto_imagenes.append(texto_imagen10)
        texto_imagenes.append(texto_imagen11)

        # Imprime el texto de cada imagen
        for i, texto in enumerate(texto_imagenes):
            print(f"Texto de imagen {i + 1}:\n{texto}\n")

        # Formatear el resultado en JSON
        resultado_json = {
            'textos_partes': texto_imagenes
        }

        return jsonify(resultado_json)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
