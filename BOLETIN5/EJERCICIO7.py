def imprimir_fichas_domino():

    # O dominó ten números dende 0 ata 6
    limite = 6

    print("--- FICHAS DE DOMINÓ ---")

    # O primeiro bucle representa o primeiro número da ficha (parte esquerda)
    for esquerda in range(limite + 1):

        # O segundo bucle representa o segundo número da ficha (parte dereita)
        # Comezamos en 'esquerda' para evitar repeticións (ex: 3-5 e 5-3)
        for dereita in range(esquerda, limite + 1):

            # Formato da ficha: [esquerda | dereita]
            print(f"[{esquerda} | {dereita}]")

# --- Programa principal ---
imprimir_fichas_domino()