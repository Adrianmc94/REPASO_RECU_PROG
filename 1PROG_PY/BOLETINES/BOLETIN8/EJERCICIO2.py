def encaixar_domino(ficha1: tuple, ficha2: tuple) -> bool:
    return ficha1[0] == ficha2[0] or ficha1[0] == ficha2[1] or ficha1[1] == ficha2[0] or ficha1[1] == ficha2[1]

# --- Exemplos de Uso ---
print(encaixar_domino((3, 4), (5, 4)))
print(encaixar_domino((1, 6), (5, 2)))
print(encaixar_domino((2, 2), (2, 5)))
print(encaixar_domino((1, 3), (3, 1)))