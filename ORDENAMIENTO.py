# Datos de ejemplo
texto_imagenes = [
    "Servicios\n\nCantidad lineas moviles disponibles para contratar\n1\n",
    "Cargo fijo maximo por linea/ pack\n$/0.00\n",
    "Método de Facturacion Adelantado\nSi\n",
    "Tipo de plan\n0\n",
    "Cargo fijo maximo por linea (movil) sin equipo financiado\n$/0.00\n",
    "Tipo de cliente\n",
    "Monto maximo Easy Pack\n$/0.00\n",
    "EQUIDOS\n\nMonto maximo a financiar equipos y accesorios\n\n$/0.00\n",
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

# Creamos un diccionario para organizar los datos
data = {}
current_category = None

for line in texto_imagenes:
    line = line.strip()

    if not line:
        continue

    # Verificamos si la línea es un título de categoría
    if line.isupper():
        current_category = line
        data[current_category] = {}
    else:
        # Verificamos si current_category no es None y si hay un par clave-valor válido
        if current_category and '\n' in line:
            key, value = line.split('\n', 1)
            data[current_category][key] = value

# Creamos la estructura JSON deseada
result_json = {
    "textos_partes": [data]
}

print(result_json)
