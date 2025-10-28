'''
Dada unha lista de números enteiros e un enteiro k, escribir unha función que:
Devolte tres listas, unha cos menores, outra cos maiores e outra cos iguais a k.
Devolte unha lista con aqueles que son múltiplos de k.
'''

def clasificar_numeros(lista_numeros: list, k: int) -> tuple:
    # Inicializamos las tres listas de salida
    menores = []
    mayores = []
    iguales_a_k = []

    # Iteramos sobre cada número de la lista
    for numero in lista_numeros:
        # Clasificamos el número respecto a k
        if numero < k:
            menores.append(numero)
        elif numero > k:
            mayores.append(numero)
        else:
            iguales_a_k.append(numero)

    # Devolvemos las tres listas como una tupla
    return (menores, mayores, iguales_a_k)

def encontrar_multiplos_de_k(lista_numeros: list, k: int) -> list:
    # Manejamos el caso especial si k es cero
    if k == 0:
        # Solo el 0 es un múltiplo (por definición), pero evitamos la división por cero
        return [n for n in lista_numeros if n == 0]

    # Usamos una comprensión de lista para filtrar los múltiplos
    # Un número es múltiplo de k si el resto de su división es 0 (numero % k == 0)
    multiplos = [numero for numero in lista_numeros if numero % k == 0]
    return multiplos

# --- Ejemplos de Uso ---

# Datos de prueba
numeros = [10, 5, 20, 15, 25, 10, 30]
k_valor = 15

# Llamada a la primera función
listas_clasificadas = clasificar_numeros(numeros, k_valor)
print(f"Clasificación (Menores, Mayores, Iguales a {k_valor}): {listas_clasificadas}")

# Llamada a la segunda función
multiplos = encontrar_multiplos_de_k(numeros, k_valor)
print(f"Múltiplos de {k_valor}: {multiplos}")