from PIL import Image
import pytesseract
from flask import Flask, request, jsonify
import base64
import io
import json
import os


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

        







        coordenadas_corte1 = (5, 0, 250, 100)
        parte_cortada1 = imagen_original.crop(coordenadas_corte1)

        coordenadas_corte2 = (coordenadas_corte1[2], 0, coordenadas_corte1[2] + 250, 100)
    
        parte_cortada2 = imagen_original.crop(coordenadas_corte2)

        coordenadas_corte3 = (coordenadas_corte2[2], 0, coordenadas_corte2[2] + 500, 100)
        parte_cortada3 = imagen_original.crop(coordenadas_corte3)

        coordenadas_corte4 = (coordenadas_corte3[2]-100, 0, coordenadas_corte3[2] +300, 90)
        parte_cortada4 = imagen_original.crop(coordenadas_corte4)

# ===========================================================================================================

        coordenadas_corte5 = (0, coordenadas_corte1[3], 300, coordenadas_corte1[3] + 60)  # Ajusta estas coordenadas para la quinta parte
        parte_cortada5 = imagen_original.crop(coordenadas_corte5)

        coordenadas_corte6 = (coordenadas_corte5[2], coordenadas_corte1[3], coordenadas_corte5[2] + 150, coordenadas_corte1[3] + 60)  # Ajusta 
        parte_cortada6 = imagen_original.crop(coordenadas_corte6)

        coordenadas_corte7 = (coordenadas_corte6[2], coordenadas_corte1[3], coordenadas_corte6[2] + 340, coordenadas_corte1[3] + 60)
        parte_cortada7 = imagen_original.crop(coordenadas_corte7)

#===========================================================================================================
        coordenadas_corte8 = (0, coordenadas_corte5[3]-10, 300, coordenadas_corte5[3] + 80)  # Ajusta estas coordenadas para la octava parte
        parte_cortada8 = imagen_original.crop(coordenadas_corte8)
    
        coordenadas_corte9 = (coordenadas_corte8[2], coordenadas_corte8[1], coordenadas_corte8[2] + 250, coordenadas_corte8[3])  # Ajusta 
        parte_cortada9 = imagen_original.crop(coordenadas_corte9)

        coordenadas_corte10 = (coordenadas_corte9[2], coordenadas_corte9[1], coordenadas_corte9[2] + 400, coordenadas_corte9[3]+10)  # Ajusta 
        parte_cortada10 = imagen_original.crop(coordenadas_corte10)

        coordenadas_corte11 = (coordenadas_corte10[2]+30, coordenadas_corte10[1], coordenadas_corte10[2] + 370, coordenadas_corte10[3]+10)  # Ajusta 
        parte_cortada11 = imagen_original.crop(coordenadas_corte11)

#===========================================================================================================
        coordenadas_corte12 = (0, coordenadas_corte8[3], 300, coordenadas_corte8[3] + 61)  # Ajusta estas coordenadas para la quinta parte
        parte_cortada12 = imagen_original.crop(coordenadas_corte12)

        coordenadas_corte13 = (coordenadas_corte12[2], coordenadas_corte12[1],  coordenadas_corte12[2]+250, coordenadas_corte12[3] )  # Ajusta estas coordenadas para la quinta parte
        parte_cortada13 = imagen_original.crop(coordenadas_corte13)

#===========================================================================================================
        coordenadas_corte14 = (0, coordenadas_corte12[3]-10, 300, coordenadas_corte12[3] + 70)  
        parte_cortada14 = imagen_original.crop(coordenadas_corte14)

        coordenadas_corte15 = (coordenadas_corte14[2], coordenadas_corte14[1],  coordenadas_corte14[2]+250, coordenadas_corte14[3] ) 
        parte_cortada15 = imagen_original.crop(coordenadas_corte15)

        coordenadas_corte16 = (coordenadas_corte15[2], coordenadas_corte15[1],  coordenadas_corte15[2]+250, coordenadas_corte15[3] ) 
        parte_cortada16 = imagen_original.crop(coordenadas_corte16)
       
        coordenadas_corte17 = (coordenadas_corte16[2]+20, coordenadas_corte16[1],  coordenadas_corte16[2]+380, coordenadas_corte16[3] ) 
        parte_cortada17 = imagen_original.crop(coordenadas_corte17)

        # Crea una lista para almacenar el texto de cada imagen
        texto_imagenes = []

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
        nueva_imagen12 = Image.new('RGB', imagen_original.size)
        nueva_imagen13 = Image.new('RGB', imagen_original.size)
        nueva_imagen14 = Image.new('RGB', imagen_original.size)
        nueva_imagen15 = Image.new('RGB', imagen_original.size)
        nueva_imagen16 = Image.new('RGB', imagen_original.size)
        nueva_imagen17 = Image.new('RGB', imagen_original.size)


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
        nueva_imagen12.paste(parte_cortada12.resize(imagen_original.size), (0, 0))
        nueva_imagen13.paste(parte_cortada13.resize(imagen_original.size), (0, 0))
        nueva_imagen14.paste(parte_cortada14.resize(imagen_original.size), (0, 0))
        nueva_imagen15.paste(parte_cortada15.resize(imagen_original.size), (0, 0))
        nueva_imagen16.paste(parte_cortada16.resize(imagen_original.size), (0, 0))
        nueva_imagen17.paste(parte_cortada17.resize(imagen_original.size), (0, 0))

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
        nueva_imagen12.save('imagen_rearmada12.jpg')
        nueva_imagen13.save('imagen_rearmada13.jpg')
        nueva_imagen14.save('imagen_rearmada14.jpg')
        nueva_imagen15.save('imagen_rearmada15.jpg')
        nueva_imagen16.save('imagen_rearmada16.jpg')
        nueva_imagen17.save('imagen_rearmada17.jpg')

        # Cierra la imagen original
        imagen_original.close()

        tesseract_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tesseract-ocr', 'tesseract.exe')

        pytesseract.pytesseract.tesseract_cmd = tesseract_dir
        # Aplica OCR para obtener el texto de cada imagen

        # Especifica la ubicación del ejecutable de Tesseract
        # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Reemplaza con la ubicación correcta de Tesseract en tu sistema

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
        imagen12 = Image.open('imagen_rearmada12.jpg')
        imagen13 = Image.open('imagen_rearmada13.jpg')
        imagen14 = Image.open('imagen_rearmada14.jpg')
        imagen15 = Image.open('imagen_rearmada15.jpg')
        imagen16 = Image.open('imagen_rearmada16.jpg')
        imagen17 = Image.open('imagen_rearmada17.jpg')


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
        texto_imagen12 = pytesseract.image_to_string(imagen12)
        texto_imagen13 = pytesseract.image_to_string(imagen13)
        texto_imagen14 = pytesseract.image_to_string(imagen14)
        texto_imagen15 = pytesseract.image_to_string(imagen15)
        texto_imagen16 = pytesseract.image_to_string(imagen16)
        texto_imagen17 = pytesseract.image_to_string(imagen17)

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
        texto_imagenes.append(texto_imagen12)
        texto_imagenes.append(texto_imagen13)
        texto_imagenes.append(texto_imagen14)
        texto_imagenes.append(texto_imagen15)
        texto_imagenes.append(texto_imagen16)
        texto_imagenes.append(texto_imagen17)


        # Imprime el texto de cada imagen
        # for i, texto in enumerate(texto_imagenes):
        #     print(f"Texto de imagen {i + 1}:\n{texto}\n")

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
        imagen12.close()
        imagen13.close()
        imagen14.close()
        imagen15.close()
        imagen16.close()
        imagen17.close()


        # Elimina las imágenes del disco duro
        imagenes_a_eliminar = [
        'imagen_rearmada1.jpg', 'imagen_rearmada2.jpg', 'imagen_rearmada3.jpg', 'imagen_rearmada4.jpg',
        'imagen_rearmada5.jpg', 'imagen_rearmada6.jpg', 'imagen_rearmada7.jpg',
        'imagen_rearmada8.jpg', 'imagen_rearmada9.jpg', 'imagen_rearmada10.jpg', 'imagen_rearmada11.jpg',
        'imagen_rearmada12.jpg', 'imagen_rearmada13.jpg',
        'imagen_rearmada14.jpg', 'imagen_rearmada15.jpg', 'imagen_rearmada16.jpg', 'imagen_rearmada17.jpg'
        ]

        for imagen in imagenes_a_eliminar:
                try:
                        os.remove(imagen)
                        print(f"Imagen {imagen} eliminada.")
                except FileNotFoundError:
                        print(f"La imagen {imagen} no se encontró.")
                except Exception as e:
                        print(f"Error al eliminar la imagen {imagen}: {e}")

        servicios1 = texto_imagen1.strip().split('\n')
        servicios2 = texto_imagen2.strip().split('\n')
        servicios3 = texto_imagen3.strip().split('\n')
        servicios4 = texto_imagen4.strip().split('\n')
        servicios5 = texto_imagen5.strip().split('\n')
        servicios6 = texto_imagen6.strip().split('\n')
        servicios7 = texto_imagen7.strip().split('\n')

        equipos1=texto_imagen8.strip().split('\n')
        equipos2=texto_imagen9.strip().split('\n')
        equipos3=texto_imagen10.strip().split('\n')
        equipos4=texto_imagen11.strip().split('\n')
        equipos5=texto_imagen12.strip().split('\n')
        equipos6=texto_imagen13.strip().split('\n')


        servicios_adicionales1=texto_imagen14.strip().split('\n')
        servicios_adicionales2=texto_imagen15.strip().split('\n')
        servicios_adicionales3=texto_imagen16.strip().split('\n')
        servicios_adicionales4=texto_imagen17.strip().split('\n')



        data = {
        "Servicios": {
                servicios1[2]: servicios1[3],
                servicios2[0]: servicios2[1],
                servicios3[0]: servicios3[1],
                servicios4[0]: servicios4[1],
                servicios5[0]: servicios5[1],
                servicios6[0]: servicios6[1]if len(servicios6) > 1 else "-",
                servicios7[0]: servicios7[1],
 
        },
        "Equipos": {
                equipos1[2]: equipos1[4],
                equipos2[0]: equipos2[1],
                equipos3[0]: equipos3[1],
                equipos4[0]: equipos4[2],
                equipos5[0]: equipos5[2],
                equipos6[0]: equipos6[1],
        },
        "Servicios_Adicionales": {
                servicios_adicionales1[2]: servicios_adicionales1[4],
                servicios_adicionales2[0]: servicios_adicionales2[1],
                servicios_adicionales3[0]: servicios_adicionales3[1],
                servicios_adicionales4[0]: servicios_adicionales4[1],
        }

        }
        json_data = json.dumps(data, ensure_ascii=False, indent=4)

        print(json_data)




        # Formatear el resultado en JSON
        resultado_json = {
        #     'textos_partes': texto_imagenes
                    'data': data


        }
        
        # print(texto_imagenes)

        return jsonify(resultado_json)
    

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
