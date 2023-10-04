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


        # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Reemplaza con la ubicación correcta de Tesseract en tu sistema

        # #=========================================================================================

        # texto = pytesseract.image_to_string(imagen_original)
        # inicio_servicio = texto.find("Servicios")

        # desplazamiento_x = 1
        # desplazamiento_y =2
        # # Si se encuentra la palabra "Servicio", recorta la imagen desde esa posición con el desplazamiento hasta el final
        # if inicio_servicio != -1:
        #     x1 = max(0, inicio_servicio - desplazamiento_x)
        #     y1 =desplazamiento_y
        #     x2 = imagen_original.width
        #     y2 = imagen_original.height

        #     imagen_recortada = imagen_original.crop((x1, y1, x2, y2))
        #     imagen_recortada.save('imagen_recortada.png')
        # Cierra la imagen original
        #imagen_original.close()
        #=========================================================================================

        # Realizar el recorte de la imagen en partes más pequeñas
        # Define las coordenadas de recorte según tus necesidades
        coordenadas_corte1 = (0, 0, 250, 100)
        parte_cortada1 = imagen_original.crop(coordenadas_corte1)

        # Define las coordenadas para cortar la segunda parte de la imagen (a la derecha de la primera)
        coordenadas_corte2 = (coordenadas_corte1[2], 0, coordenadas_corte1[2] + 250, 100)
        parte_cortada2 = imagen_original.crop(coordenadas_corte2)

        # Define las coordenadas para cortar la tercera parte de la imagen (a la derecha de la segunda)
        coordenadas_corte3 = (coordenadas_corte2[2], 0, coordenadas_corte2[2] + 350, 100)
        parte_cortada3 = imagen_original.crop(coordenadas_corte3)

        # Define las coordenadas para cortar la tercera parte de la imagen (a la derecha de la segunda)
        coordenadas_corte4 = (coordenadas_corte3[2], 0, coordenadas_corte3[2] + 350, 100)
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
        coordenadas_corte10 = (coordenadas_corte9[2], coordenadas_corte9[1], coordenadas_corte9[2] + 340, coordenadas_corte9[3])  # Ajusta estas coordenadas para la novena parte

        # Corta la novena parte deseada de la imagen original
        parte_cortada10 = imagen_original.crop(coordenadas_corte10)

        # Define las coordenadas para cortar la novena parte de la imagen (al costado del corte 8)
        coordenadas_corte11 = (coordenadas_corte10[2], coordenadas_corte10[1], coordenadas_corte10[2] + 370, coordenadas_corte10[3])  # Ajusta estas coordenadas para la novena parte

        # Corta la novena parte deseada de la imagen original
        parte_cortada11 = imagen_original.crop(coordenadas_corte11)

        # Define el nuevo tamaño de las imágenes (el tamaño de las partes cortadas)
        nuevo_ancho, nuevo_alto = parte_cortada1.size

        # Crea tres nuevas imágenes vacías con el tamaño deseado (el tamaño de la imagen original)
        nueva_imagen1 = Image.new('RGB', imagen_original.size)
        nueva_imagen2 = Image.new('RGB', imagen_original.size)
        nueva_imagen3 = Image.new('RGB', imagen_original.size)
        nueva_imagen4 = Image.new('RGB', imagen_original.size)
        nueva_imagen5 = Image.new('RGB', imagen_original.size)
        nueva_imagen6 = Image.new('RGB', imagen_original.size)
        nueva_imagen7 = Image.new('RGB', imagen_original.size)
        nueva_imagen8 = Image.new('RGB', imagen_original.size)
        nueva_imagen9 = Image.new('RGB', imagen_original.size)
        nueva_imagen10 = Image.new('RGB', imagen_original.size)
        nueva_imagen11 = Image.new('RGB', imagen_original.size)


        # Pega las partes cortadas en las nuevas imágenes escalándolas al tamaño de la imagen original
        nueva_imagen1.paste(parte_cortada1.resize(imagen_original.size), (0, 0))
        nueva_imagen2.paste(parte_cortada2.resize(imagen_original.size), (0, 0))
        nueva_imagen3.paste(parte_cortada3.resize(imagen_original.size), (0, 0))
        nueva_imagen4.paste(parte_cortada4.resize(imagen_original.size), (0, 0))
        nueva_imagen5.paste(parte_cortada5.resize(imagen_original.size), (0, 0))
        nueva_imagen6.paste(parte_cortada6.resize(imagen_original.size), (0, 0))
        nueva_imagen7.paste(parte_cortada7.resize(imagen_original.size), (0, 0))
        nueva_imagen8.paste(parte_cortada8.resize(imagen_original.size), (0, 0))
        nueva_imagen9.paste(parte_cortada9.resize(imagen_original.size), (0, 0))
        nueva_imagen10.paste(parte_cortada10.resize(imagen_original.size), (0, 0))
        nueva_imagen11.paste(parte_cortada11.resize(imagen_original.size), (0, 0))


        # Guarda las nuevas imágenes
        nueva_imagen1.save('imagen_rearmada1.jpg')
        nueva_imagen2.save('imagen_rearmada2.jpg')
        nueva_imagen3.save('imagen_rearmada3.jpg')
        nueva_imagen4.save('imagen_rearmada4.jpg')
        nueva_imagen5.save('imagen_rearmada5.jpg')
        nueva_imagen6.save('imagen_rearmada6.jpg')
        nueva_imagen7.save('imagen_rearmada7.jpg')
        nueva_imagen8.save('imagen_rearmada8.jpg')
        nueva_imagen9.save('imagen_rearmada9.jpg')
        nueva_imagen10.save('imagen_rearmada10.jpg')
        nueva_imagen11.save('imagen_rearmada11.jpg')

        # Cierra la imagen original
        imagen_original.close()

        # Especifica la ubicación del ejecutable de Tesseract
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Reemplaza con la ubicación correcta de Tesseract en tu sistema

        # Abre las imágenes recortadas
        imagen1 = Image.open('imagen_rearmada1.jpg')
        imagen2 = Image.open('imagen_rearmada2.jpg')
        imagen3 = Image.open('imagen_rearmada3.jpg')
        imagen4 = Image.open('imagen_rearmada4.jpg')
        imagen5 = Image.open('imagen_rearmada5.jpg')
        imagen6 = Image.open('imagen_rearmada6.jpg')
        imagen7 = Image.open('imagen_rearmada7.jpg')
        imagen8 = Image.open('imagen_rearmada8.jpg')
        imagen9 = Image.open('imagen_rearmada9.jpg')
        imagen10 = Image.open('imagen_rearmada10.jpg')
        imagen11 = Image.open('imagen_rearmada11.jpg')

        # Crea una lista para almacenar el texto de cada imagen
        texto_imagenes = []

        # Aplica OCR para obtener el texto de cada imagen
        texto_imagen1 = pytesseract.image_to_string(imagen1)
        texto_imagen2 = pytesseract.image_to_string(imagen2)
        texto_imagen3 = pytesseract.image_to_string(imagen3)
        texto_imagen4 = pytesseract.image_to_string(imagen4)
        texto_imagen5 = pytesseract.image_to_string(imagen5)
        texto_imagen6 = pytesseract.image_to_string(imagen6)
        texto_imagen7 = pytesseract.image_to_string(imagen7)
        texto_imagen8 = pytesseract.image_to_string(imagen8)
        texto_imagen9 = pytesseract.image_to_string(imagen9)
        texto_imagen10 = pytesseract.image_to_string(imagen10)
        texto_imagen11 = pytesseract.image_to_string(imagen11)

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

        # Cierra las imágenes
        imagen1.close()
        imagen2.close()
        imagen3.close()
        imagen4.close()
        imagen5.close()
        imagen6.close()
        imagen7.close()
        imagen8.close()
        imagen9.close()
        imagen10.close()
        imagen11.close()

        # Formatear el resultado en JSON
        resultado_json = {
            'textos_partes': texto_imagenes
        }

        return jsonify(resultado_json)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
