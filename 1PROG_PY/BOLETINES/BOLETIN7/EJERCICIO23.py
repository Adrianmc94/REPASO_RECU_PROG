def analizar_texto(texto: str):
    palabras = texto.split()
    num_caracteres = len(texto)
    num_palabras = len(palabras)

    palabra_mais_longa = ""
    if palabras:
        palabra_mais_longa = max(palabras, key=len)

    print("--- Análise de Texto ---")
    print(f"Número de Caracteres (incluíndo espazos): {num_caracteres}")
    print(f"Número de Palabras: {num_palabras}")
    print(f"Palabra máis longa: '{palabra_mais_longa}' (Lonxitude: {len(palabra_mais_longa)})")

texto_exemplo = "Este é un exemplo simple de análise de texto."
analizar_texto(texto_exemplo)

print("\n")

texto_vacio = "   "
analizar_texto(texto_vacio)