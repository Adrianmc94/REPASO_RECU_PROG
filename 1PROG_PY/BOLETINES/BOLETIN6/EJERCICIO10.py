# Definición de las matrices A y B según las especificaciones:
# Lista de tuplas, donde cada tupla es una fila.

A = ((1, 2, 3),
     (4, 5, 6))

B = ((-1, 0),
     (0, 1),
     (1, 1))

# Almacenar las matrices en una lista
matrices = [A, B]

# --- Función para multiplicar dos matrices (A_m_n * B_n_p = C_m_p) ---
def producto_matrices(mat1, mat2):

    filas_A = len(mat1)
    cols_A = len(mat1[0])
    filas_B = len(mat2)
    cols_B = len(mat2[0])

    if cols_A != filas_B:
        return "Error: El número de columnas de la primera matriz no coincide con el número de filas de la segunda."

    # Inicializar la matriz resultado C (m x p) con ceros
    # Usaremos una lista de listas para la construcción, ya que las tuplas son inmutables
    C = [[0 for _ in range(cols_B)] for _ in range(filas_A)]

    # Calcular el producto elemento por elemento
    for i in range(filas_A):
        for j in range(cols_B):
            suma_producto = 0
            for k in range(cols_A):
                suma_producto += mat1[i][k] * mat2[k][j]
            C[i][j] = suma_producto
    return C

# Calcular el producto
producto = producto_matrices(A, B)


print(f"Matriz A (representada como lista de tuplas):\n{A}")
print(f"Matriz B (representada como lista de tuplas):\n{B}")
print(f"Lista que contiene las matrices: {matrices}")
print("\nProducto de A * B:")
if isinstance(producto, str):
    print(producto)
else:
    # Mostrar la matriz resultado formateada
    for fila in producto:
        print(fila)
