# --------------------------------------------
# Ejercicio 3: Ordenar lista de llegadas (Insertion Sort)
# --------------------------------------------

tiempos = [58, 54, 60, 52, 57, 56, 59]
comparaciones = 0
intercambios = 0

print("\nTiempos originales:")
print(tiempos)

for i in range(1, len(tiempos)):
    actual = tiempos[i]
    j = i - 1
    while j >= 0 and tiempos[j] > actual:
        comparaciones += 1
        tiempos[j+1] = tiempos[j]
        intercambios += 1
        j -= 1
    tiempos[j+1] = actual
    print(f"Después de insertar {actual}: {tiempos}")

print("\nTiempos ordenados (de menor a mayor):")
print(tiempos)

print(f"\nComparaciones: {comparaciones}")
print(f"Intercambios: {intercambios}")