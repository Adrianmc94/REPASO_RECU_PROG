'''
Escribir unha función que reciba unha lista de tuplas (Apelido, Nome, Inicial_segundo_nome)
e devolte unha lista de cadenas onde cada unha conteña primero o nome, logo a inicial cun punto, e logo o apelido.
'''
def formatar_nomes_completos(lista_personas: list) -> list:
    nombres_formateados = []

    # La tupla de entrada se desestructura en (Apelido, Nome, Inicial)
    for apellido, nombre, inicial in lista_personas:
        # Crea la cadena con el formato: Nombre Inicial. Apelido
        cadena_formateada = f"{nombre} {inicial}. {apellido}"
        nombres_formateados.append(cadena_formateada)

    return nombres_formateados

# --- Ejemplos de Uso ---
datos = [
    ("Perez", "Juan", "G"),
    ("Garcia", "Ana", "L"),
    ("Lopez", "Carlos", "M")
]

resultado = formatar_nomes_completos(datos)
print(resultado)