def imprimir_numeros_triangulares(n):

    # Inicializamos a suma_acumulada (o número triangular) a 0
    suma_acumulada = 0

    for indice in range(1, n + 1):

        # O número triangular actual é a suma do número triangular anterior
        # máis o índice actual.
        suma_acumulada += indice

        # Imprimimos o índice (n) e o número triangular resultante
        print(f"{indice} - {suma_acumulada}")

# --- Programa principal ---

while True:
    try:
        # Solicitamos ao usuario cantos números triangulares quere (o valor de n)
        n = int(input("Introduce a cantidade de números triangulares (n): "))

        if n <= 0:
            print("Por favor, introduce un número enteiro positivo.")
        else:
            print(f"\nOs primeiros {n} números triangulares son:")
            imprimir_numeros_triangulares(n)
            break

    except ValueError:
        print("Erro: A entrada non é un número enteiro válido. Téntao de novo.")