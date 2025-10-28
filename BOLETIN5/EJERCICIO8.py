def imprimir_fichas_domino_xeral():

    while True:
        try:
            limite_maximo = int(input("Introduce o número máximo (n) para as fichas de dominó (ex: 6 para un xogo estándar): "))

            if limite_maximo < 0:
                print("O límite máximo debe ser un número enteiro non negativo.")
                continue

            break
        except ValueError:
            print("Erro: Entrada non válida. Introduce un número enteiro.")

    print(f"\n--- FICHAS DE DOMINÓ (0 a {limite_maximo}) ---")

    # O bucle externo vai dende 0 ata o límite máximo (n)
    for esquerda in range(limite_maximo + 1):

        # O bucle interno vai dende 'esquerda' ata o límite máximo
        # para asegurar que non haxa repeticións (ex: evita [3|5] se xa se imprimiu [5|3])
        for dereita in range(esquerda, limite_maximo + 1):

            print(f"[{esquerda} | {dereita}]")

# --- Programa principal ---
imprimir_fichas_domino_xeral()