# --------------------------------------------
# Ejercicio 3: Ordenar lista de llegadas (Insertion Sort)
# --------------------------------------------

# Lista de tiempos de llegada de corredores en segundos
tiempos = [58, 54, 60, 52, 57, 56, 59]
comparaciones = 0  # Contador de comparaciones realizadas
intercambios = 0   # Contador de intercambios/desplazamientos realizados

print("\nTiempos originales:")
print(tiempos)

# ALGORITMO INSERTION SORT
# -------------------------
# Insertion Sort construye una sublista ordenada insertando un elemento
# a la vez. Toma cada nuevo elemento y lo inserta en su posicion correcta
# dentro de la sublista ya ordenada, desplazando los elementos mayores
# hacia la derecha. Es ideal para datos que llegan en tiempo real.

# Comenzar desde el segundo elemento (indice 1)
for i in range(1, len(tiempos)):
    actual = tiempos[i]  # Elemento actual a insertar
    j = i - 1           # Indice del ultimo elemento en la sublista ordenada
    
    # Desplazar elementos de la sublista ordenada que son mayores que 'actual'
    while j >= 0 and tiempos[j] > actual:
        comparaciones += 1    # Incrementar contador de comparaciones
        tiempos[j+1] = tiempos[j]  # Desplazar elemento hacia la derecha
        intercambios += 1     # Incrementar contador de desplazamientos
        j -= 1                # Mover al elemento anterior
    
    # Insertar el elemento actual en su posicion correcta
    tiempos[j+1] = actual
    
    # Mostrar el estado del arreglo despues de insertar cada elemento
    print(f"Despues de insertar {actual}: {tiempos}")

print("\nTiempos ordenados (de menor a mayor):")
print(tiempos)

# Mostrar estadisticas finales del algoritmo
print(f"\nComparaciones: {comparaciones}")
print(f"Intercambios: {intercambios}")