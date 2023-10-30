import re

import re

# Datos de ejemplo
texto_imagenes = [
    "Servicios\n\nCantidad lineas moviles disponibles para contratar\n1\n",
    "Cargo fijo maximo por linea/ pack\n$/0.00\n",
    "Método de Facturacion Adelantado\nSi\n",
    "Tipo de plan\n0\n",
    "Cargo fijo maximo por linea (movil) sin equipo financiado\n$/0.00\n",
    "Tipo de cliente\n",
    "Monto maximo Easy Pack\n$/0.00\n",
    "Equipos\n\nMonto maximo a financiar equipos y accesorios\n\n$/0.00\n",
    "Monto ocupado en financiamiento\n\n$/0.00\n",
    "Monto disponible para financiamiento de equipos y acessorios\n$/0.00\n",
    "Cantidad de meses para financiamiento equipos y accesorios\n\n0\n\n",
    "Ratio de Financiamiento\n\n0%\n",
    "Tipo de cliente VEP\n0\n",
    "Servicios Adicionales\n\nMonto disponible para contratar servicios adicionales\n\n$/0.00\n",
    "Monto disponible en primas de seguros\n$/0.00\n",
    "Cupo servicios complementari\n$/0.00\n",
    "Monto para acreditar deuda portabilidad\n$/0.00\n"
]

# Función para dividir el texto en categorías y pares clave-valor
def extract_data(text):
    data = {}
    current_category = None

    for line in text:
        line = line.strip()
        if re.match(r'^[A-Z].*$', line):
            current_category = line
            data[current_category] = {}
        elif current_category:
            key, value = line.split('\n', 1)
            data[current_category][key] = value

    return data

# Extraer los datos
data = extract_data(texto_imagenes)

# Crear una estructura JSON con las categorías deseadas
result_json = {
    "textos_partes": [data]
}

# Crear una estructura JSON con las subcategorías
categories_mapping = {
    "Servicios": ["Cantidad lineas moviles disponibles para contratar", "Cargo fijo maximo por linea/ pack", "Método de Facturacion Adelantado", "Tipo de plan", "Cargo fijo maximo por linea (movil) sin equipo financiado", "Tipo de cliente", "Monto maximo Easy Pack"],
    "Equipos": ["Monto maximo a financiar equipos y accesorios", "Monto ocupado en financiamiento", "Monto disponible para financiamiento de equipos and acessorios", "Cantidad de meses para financiamiento equipos y acessorios", "Ratio de Financiamiento", "Tipo de cliente VEP"],
    "Servicios Adicionales": ["Monto disponible para contratar servicios adicionales", "Monto disponible en primas de seguros", "Cupo servicios complementari", "Monto para acreditar deuda portabilidad"]
}

final_result = {"textos_partes": [{}]}

for category_name, subcategories in categories_mapping.items():
    final_result["textos_partes"][0][category_name] = {}
    for subcategory in subcategories:
        if subcategory in data.get(category_name, {}):
            final_result["textos_partes"][0][category_name][subcategory] = data[category_name].get(subcategory, '')

# Verificar si alguna de las categorías está completamente vacía y eliminarla
final_result["textos_partes"][0] = {k: v for k, v in final_result["textos_partes"][0].items() if v}

# Imprimir el resultado
print(final_result)

