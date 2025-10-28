'''
Escribir unha función empaquetar para unha lista,
onde empaquetar significa indicar a repetición de valores consecutivos mediante unha tupla
(valor, cantidade de repeticións). Por exemplo, empaquetar ([1, 1, 1, 3, 5, 1, 1, 3, 3]) debe devoltar [(1, 3) , (3, 1) , (5, 1), (1, 2), (3, 2)].
'''
def empaquetar_lista(lista_entrada: list) -> list:
    if not lista_entrada:
        return []

    resultado = []
    valor_actual = lista_entrada[0]
    contador = 1

    for i in range(1, len(lista_entrada)):
        if lista_entrada[i] == valor_actual:
            contador += 1
        else:
            resultado.append((valor_actual, contador))
            valor_actual = lista_entrada[i]
            contador = 1

    # Engade o último grupo que non se engadiu no bucle
    resultado.append((valor_actual, contador))

    return resultado

# --- Exemplos de Uso ---
print(empaquetar_lista([1, 1, 1, 3, 5, 1, 1, 3, 3]))
print(empaquetar_lista(['a', 'a', 'b', 'c', 'c', 'c', 'a']))
print(empaquetar_lista([]))