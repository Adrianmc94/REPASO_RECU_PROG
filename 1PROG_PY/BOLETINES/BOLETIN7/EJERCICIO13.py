def substituir_espazos(cadea: str, caracter: str, max_operacions: int = -1) -> str:
    if max_operacions <= 0:
        return cadea.replace(' ', caracter)

    partes = cadea.split(' ', max_operacions)
    if len(partes) > max_operacions:
        base = caracter.join(partes[:-1])
        return base + caracter + partes[-1]
    else:
        return caracter.join(partes)

def inserir_entre_letras(cadea: str, caracter: str, max_operacions: int = -1) -> str:
    if max_operacions <= 0:
        return caracter.join(cadea)

    limite = min(len(cadea) - 1, max_operacions)

    return caracter.join(cadea[:limite+1]) + cadea[limite+1:]

def substituir_digitos(cadea: str, caracter: str, max_operacions: int = -1) -> str:
    nova_cadea = ""
    contador = 0
    for letra in cadea:
        if letra.isdigit():
            if max_operacions <= 0 or contador < max_operacions:
                nova_cadea += caracter
                contador += 1
            else:
                nova_cadea += letra
        else:
            nova_cadea += letra
    return nova_cadea

def inserir_cada_tres_digitos(cadea: str, caracter: str, max_operacions: int = -1) -> str:
    digitos = "".join(letra for letra in cadea if letra.isdigit())

    if max_operacions <= 0:
        texto_a_formatear = digitos
        resto_digitos = ""
    else:
        num_grupos = max_operacions
        digitos_a_procesar = num_grupos * 3

        texto_a_formatear = digitos[:digitos_a_procesar]
        resto_digitos = digitos[digitos_a_procesar:]

    partes = []
    for i in range(0, len(texto_a_formatear), 3):
        partes.append(texto_a_formatear[i:i+3])

    resultado_formateado = caracter.join(partes)

    return resultado_formateado + resto_digitos

# --- Pruebas ---
print(substituir_espazos('meu arquivo de texto.txt', '_', 1))
print(inserir_entre_letras('separar', ',', 2))
print(substituir_digitos('sua clave é: 1540', 'X', 2))
print(inserir_cada_tres_digitos('2552552550', '.', 2))