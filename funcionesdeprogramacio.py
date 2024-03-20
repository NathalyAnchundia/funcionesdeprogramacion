def calcular_temperatura_promedio(temperaturas):
    """
    Calcula la temperatura promedio de cada ciudad durante un período de tiempo.

    Args:
        temperaturas (list): Una lista tridimensional que contiene las temperaturas de las ciudades y semanas.

    Returns:
        list: Una lista que contiene las temperaturas promedio de cada ciudad.
    """
    promedios = []
    for ciudad_temperaturas in temperaturas:
        promedio_ciudad = sum(sum(semana) for semana in ciudad_temperaturas) / (len(ciudad_temperaturas) * len(ciudad_temperaturas[0]))
        promedios.append(promedio_ciudad)
    return promedios

# Ejemplo de datos de temperaturas
temperaturas = [
    [  # Ciudad 1
        [25, 26, 24, 23, 22, 21, 20],  # Semana 1
        [24, 23, 25, 26, 27, 28, 22],  # Semana 2
        [23, 22, 24, 25, 26, 27, 28],  # Semana 3
    ],
    [  # Ciudad 2
        [22, 23, 24, 25, 26, 27, 28],  # Semana 1
        [23, 24, 25, 26, 27, 28, 29],  # Semana 2
        [24, 25, 26, 27, 28, 29, 30],  # Semana 3
    ],
    [  # Ciudad 3
        [20, 21, 22, 23, 24, 25, 26],  # Semana 1
        [21, 22, 23, 24, 25, 26, 27],  # Semana 2
        [22, 23, 24, 25, 26, 27, 28],  # Semana 3
    ],
]

# Calcular temperaturas promedio por ciudad
temperaturas_promedio = calcular_temperatura_promedio(temperaturas)

# Mostrar los resultados
for i, promedio_ciudad in enumerate(temperaturas_promedio):
    print(f"La temperatura promedio de la Ciudad {i+1} es: {promedio_ciudad}°C")