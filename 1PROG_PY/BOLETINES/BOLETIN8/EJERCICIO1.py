def verificar_orden_simple(tupla_elementos: tuple) -> bool:
    # A función sorted() devolve unha NOVA LISTA cos elementos ordenados.
    return list(tupla_elementos) == sorted(tupla_elementos)

# --- Exemplo de Uso ---
print(verificar_orden_simple((1, 5, 10, 15))) # True
print(verificar_orden_simple((1, 10, 5, 15))) # False