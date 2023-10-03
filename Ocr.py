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

        # Define el nuevo tamaño de las imágenes (el tamaño de las partes cortadas)
        nuevo_ancho, nuevo_alto = parte_cortada1.size

        # Crea tres nuevas imágenes vacías con el tamaño deseado (el tamaño de la imagen original)
        nueva_imagen1 = Image.new('RGB', imagen_original.size)
        nueva_imagen2 = Image.new('RGB', imagen_original.size)
        nueva_imagen3 = Image.new('RGB', imagen_original.size)
        nueva_imagen4 = Image.new('RGB', imagen_original.size)

        # Pega las partes cortadas en las nuevas imágenes escalándolas al tamaño de la imagen original
        nueva_imagen1.paste(parte_cortada1.resize(imagen_original.size), (0, 0))
        nueva_imagen2.paste(parte_cortada2.resize(imagen_original.size), (0, 0))
        nueva_imagen3.paste(parte_cortada3.resize(imagen_original.size), (0, 0))
        nueva_imagen4.paste(parte_cortada4.resize(imagen_original.size), (0, 0))

        # Guarda las nuevas imágenes
        nueva_imagen1.save('imagen_rearmada1.jpg')
        nueva_imagen2.save('imagen_rearmada2.jpg')
        nueva_imagen3.save('imagen_rearmada3.jpg')
        nueva_imagen4.save('imagen_rearmada4.jpg')

        # Cierra la imagen original
        imagen_original.close()

        # Especifica la ubicación del ejecutable de Tesseract
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Reemplaza con la ubicación correcta de Tesseract en tu sistema

        # Abre las imágenes recortadas
        imagen1 = Image.open('imagen_rearmada1.jpg')
        imagen2 = Image.open('imagen_rearmada2.jpg')
        imagen3 = Image.open('imagen_rearmada3.jpg')
        imagen4 = Image.open('imagen_rearmada4.jpg')

        # Crea una lista para almacenar el texto de cada imagen
        texto_imagenes = []

        # Aplica OCR para obtener el texto de cada imagen
        texto_imagen1 = pytesseract.image_to_string(imagen1)
        texto_imagen2 = pytesseract.image_to_string(imagen2)
        texto_imagen3 = pytesseract.image_to_string(imagen3)
        texto_imagen4 = pytesseract.image_to_string(imagen4)

        # Agrega el texto de cada imagen a la lista
        texto_imagenes.append(texto_imagen1)
        texto_imagenes.append(texto_imagen2)
        texto_imagenes.append(texto_imagen3)
        texto_imagenes.append(texto_imagen4)

        # Imprime el texto de cada imagen
        for i, texto in enumerate(texto_imagenes):
            print(f"Texto de imagen {i + 1}:\n{texto}\n")

        # Cierra las imágenes
        imagen1.close()
        imagen2.close()
        imagen3.close()
        imagen4.close()

        # Formatear el resultado en JSON
        resultado_json = {
            'textos_partes': texto_imagenes
        }

        return jsonify(resultado_json)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
