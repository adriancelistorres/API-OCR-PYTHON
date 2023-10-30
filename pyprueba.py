# Supongamos que tienes la respuesta en una lista llamada "textos_partes"
textos_partes = [
    "Servicios\n\nCantidad lineas moviles disponibles para contratar\na |\n",
    # Otros elementos de la lista...
]

# Crear un diccionario para almacenar los resultados
resultados = {}

# Iterar a través de cada elemento en la lista
for texto in textos_partes:
    # Dividir el texto en líneas separadas
    lineas = texto.strip().split('\n\n')

    # Tomar el primer elemento como clave y el segundo como valor
    clave = lineas[1].strip()
    valor = lineas[-1].strip()

    # Agregar al diccionario
    resultados[clave] = valor

# Mostrar los resultados
for clave, valor in resultados.items():
    print(f"{clave} : {valor}")
