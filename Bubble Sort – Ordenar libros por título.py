# --------------------------------------------
# Ejercicio 1: Ordenar Libros por Título (Bubble Sort)
# --------------------------------------------

libros = [
    {"Id": 1, "Titulo": "Cien años de soledad", "Autor": "Gabriel García Márquez"},
    {"Id": 2, "Titulo": "Don Quijote de la Mancha", "Autor": "Miguel de Cervantes"},
    {"Id": 3, "Titulo": "La sombra del viento", "Autor": "Carlos Ruiz Zafón"},
    {"Id": 4, "Titulo": "1984", "Autor": "George Orwell"},
    {"Id": 5, "Titulo": "El principito", "Autor": "Antoine de Saint-Exupéry"}
]

n = len(libros)
comparaciones = 0
intercambios = 0

print("Arreglo original:")
for libro in libros:
    print(libro["Titulo"])
print()

# Algoritmo Bubble Sort
for i in range(n-1):
    for j in range(n-1-i):
        comparaciones += 1
        if libros[j]["Titulo"].lower() > libros[j+1]["Titulo"].lower():
            # Intercambio
            libros[j], libros[j+1] = libros[j+1], libros[j]
            intercambios += 1
    # Mostrar el arreglo después de cada pasada
    print(f"Pasada {i+1}: {[libro['Titulo'] for libro in libros]}")

print("\nLibros ordenados alfabéticamente:")
for libro in libros:
    print(libro["Titulo"])

print(f"\nComparaciones: {comparaciones}")
print(f"Intercambios: {intercambios}")