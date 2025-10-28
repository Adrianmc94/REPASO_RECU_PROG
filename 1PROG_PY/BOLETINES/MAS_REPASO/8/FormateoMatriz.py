'''
Enunciado: Escribir una función que reciba una matriz (lista de listas de números) y devuelva una lista
con la suma de los elementos de cada columna que tenga un índice impar (índice 1, 3, 5, etc.).
'''
def sumar_columnas_impares(matriz: list) -> list:

    if not matriz or not matriz[0]:
        return []

    filas = len(matriz)
    columnas = len(matriz[0])

    sumas_impares = []

    # Iteración sobre los índices de las columnas
    for j in range(columnas):
        # Condición para columnas con índice impar
        if j % 2 != 0:
            suma_columna = 0
            # Sumar todos los elementos de esa columna
            for i in range(filas):
                suma_columna += matriz[i][j]

            sumas_impares.append(suma_columna)

    return sumas_impares

print(sumar_columnas_impares([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(sumar_columnas_impares([[10, 20, 30, 40], [50, 60, 70, 80]]))