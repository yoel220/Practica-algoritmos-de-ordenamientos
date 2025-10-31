# --------------------------------------------
# Ejercicio 1: Ordenar Libros por Titulo (Bubble Sort)
# --------------------------------------------

# Lista de libros con informacion de ID, Titulo y Autor
libros = [
    {"Id": 1, "Titulo": "Cien anos de soledad", "Autor": "Gabriel Garcia Marquez"},
    {"Id": 2, "Titulo": "Don Quijote de la Mancha", "Autor": "Miguel de Cervantes"},
    {"Id": 3, "Titulo": "La sombra del viento", "Autor": "Carlos Ruiz Zafon"},
    {"Id": 4, "Titulo": "1984", "Autor": "George Orwell"},
    {"Id": 5, "Titulo": "El principito", "Autor": "Antoine de Saint-Exupery"}
]

n = len(libros)
comparaciones = 0  # Contador de comparaciones realizadas
intercambios = 0   # Contador de intercambios realizados

print("Arreglo original:")
for libro in libros:
    print(libro["Titulo"])
print()

# ALGORITMO BUBBLE SORT
# ----------------------
# Bubble Sort funciona comparando elementos adyacentes e intercambiandolos
# si estan en el orden incorrecto. Este proceso se repite hasta que no se
# necesiten mas intercambios, indicando que la lista esta ordenada.

for i in range(n-1):
    # Cada pasada reduce el rango de comparacion ya que los elementos
    # mas grandes ya estan en su posicion final
    for j in range(n-1-i):
        comparaciones += 1  # Incrementar contador de comparaciones
        
        # Comparar titulos en minusculas para ordenamiento case-insensitive
        if libros[j]["Titulo"].lower() > libros[j+1]["Titulo"].lower():
            # Intercambiar elementos si estan en orden incorrecto
            libros[j], libros[j+1] = libros[j+1], libros[j]
            intercambios += 1  # Incrementar contador de intercambios
    
    # Mostrar el estado del arreglo despues de cada pasada completa
    print(f"Pasada {i+1}: {[libro['Titulo'] for libro in libros]}")

print("\nLibros ordenados alfabeticamente:")
for libro in libros:
    print(libro["Titulo"])

# Mostrar estadisticas finales del algoritmo
print(f"\nComparaciones: {comparaciones}")
print(f"Intercambios: {intercambios}")