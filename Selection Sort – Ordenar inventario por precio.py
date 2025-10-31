# --------------------------------------------
# Ejercicio 2: Ordenar Inventario por Precio (Selection Sort)
# --------------------------------------------

# Lista de precios de productos en pesos dominicanos
precios = [250, 120, 75, 300, 100, 180, 90, 220]
n = len(precios)
comparaciones = 0  # Contador de comparaciones realizadas
intercambios = 0   # Contador de intercambios realizados

print("\nPrecios originales:")
print(precios)

# ALGORITMO SELECTION SORT
# -------------------------
# Selection Sort divide la lista en dos partes: una sublista ordenada que
# se construye de izquierda a derecha, y una sublista desordenada con los
# elementos restantes. En cada iteracion, encuentra el elemento minimo de
# la sublista desordenada y lo intercambia con el primer elemento de dicha sublista.

for i in range(n-1):
    min_index = i  # Suponer que el primer elemento es el minimo
    
    # Buscar el elemento minimo en la sublista desordenada
    for j in range(i+1, n):
        comparaciones += 1  # Incrementar contador de comparaciones
        
        # Si encontramos un elemento menor, actualizar el indice minimo
        if precios[j] < precios[min_index]:
            min_index = j
    
    print(f"Iteracion {i+1}: minimo encontrado en indice {min_index} (valor: {precios[min_index]})")
    
    # Intercambiar el elemento minimo encontrado con el primer elemento
    # de la sublista desordenada, solo si son diferentes
    if min_index != i:
        precios[i], precios[min_index] = precios[min_index], precios[i]
        intercambios += 1  # Incrementar contador de intercambios
    
    # Mostrar el estado actual del arreglo despues de cada iteracion
    print(f"Estado actual: {precios}")

print("\nPrecios ordenados:")
print(precios)

# Mostrar estadisticas finales del algoritmo
print(f"\nComparaciones: {comparaciones}")
print(f"Intercambios: {intercambios}")