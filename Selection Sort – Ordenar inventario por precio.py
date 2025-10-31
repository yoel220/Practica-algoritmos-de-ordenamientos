# --------------------------------------------
# Ejercicio 2: Ordenar Inventario por Precio (Selection Sort)
# --------------------------------------------

precios = [250, 120, 75, 300, 100, 180, 90, 220]
n = len(precios)
comparaciones = 0
intercambios = 0

print("\nPrecios originales:")
print(precios)

for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        comparaciones += 1
        if precios[j] < precios[min_index]:
            min_index = j
    print(f"Iteración {i+1}: mínimo encontrado en índice {min_index}")
    
    # Intercambiar si es necesario
    if min_index != i:
        precios[i], precios[min_index] = precios[min_index], precios[i]
        intercambios += 1
    
    print(f"Estado actual: {precios}")

print("\nPrecios ordenados:")
print(precios)
print(f"\nComparaciones: {comparaciones}")
print(f"Intercambios: {intercambios}")