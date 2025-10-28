'''
Matrices.
Escribir unha función que reciba duas matrices e devolte a suma.
Escribir unha función que reciba duas matrices e devolte o produto.
'''
import numpy as np

def sumar_matrices(matriz_a: list, matriz_b: list) -> list:
    # Asumo que as matrices son listas de listas
    filas = len(matriz_a)
    cols = len(matriz_a[0])

    matriz_suma = [[0 for _ in range(cols)] for _ in range(filas)]

    for i in range(filas):
        for j in range(cols):
            matriz_suma[i][j] = matriz_a[i][j] + matriz_b[i][j]

    return matriz_suma

def produto_matrices(matriz_a: list, matriz_b: list) -> list:
    # Usamos numpy para o produto matricial (requírese instalar numpy)
    np_a = np.array(matriz_a)
    np_b = np.array(matriz_b)

    # O operador @ realiza a multiplicación matricial
    resultado_np = np_a @ np_b

    # Convertemos o resultado de volta a unha lista de listas (formato orixinal)
    return resultado_np.tolist()

# --- Exemplos de Uso ---
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Suma
suma = sumar_matrices(A, B)
print(f"Suma de A + B: {suma}")

# Produto (require que as dimensións sexan compatibles: (m x n) * (n x p))
C = [[1, 0, 1], [0, 2, 1]] # 2x3
D = [[1, 2], [3, 4], [5, 6]] # 3x2
produto = produto_matrices(C, D)
print(f"Produto de C * D: {produto}")