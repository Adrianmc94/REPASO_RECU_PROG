'''
Enunciado: Escribir una función que reciba una lista de fichas de dominó (tuplas) y la devuelva ordenada. Las fichas que contengan el valor máximo
de toda la lista deben ir primero, y el resto después. Dentro de cada grupo, la ordenación debe ser alfabética (lexicográfica).
'''
def ordenar_fichas_encaixables(fichas: list) -> list:

    # Encuentra el valor más grande en cualquiera de los lados de todas las fichas
    max_valor = max(max(f) for f in fichas)

    fichas_encaixables = []
    fichas_non_encaixables = []

    # Clasifica las fichas en dos grupos
    for ficha in fichas:
        if max_valor in ficha:
            fichas_encaixables.append(ficha)
        else:
            fichas_non_encaixables.append(ficha)

    # Ordena alfabéticamente cada grupo
    fichas_encaixables.sort()
    fichas_non_encaixables.sort()

    # Devuelve la lista combinada (encaixables primero)
    return fichas_encaixables + fichas_non_encaixables

print(ordenar_fichas_encaixables([(1, 4), (5, 3), (4, 3), (6, 0)]))
