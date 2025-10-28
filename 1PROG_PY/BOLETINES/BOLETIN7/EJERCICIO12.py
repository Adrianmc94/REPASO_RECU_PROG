

def sustituir_espacios(cadena: str, caracter: str) -> str:
        return cadena.replace(" ", caracter)

def insertar_entre_letras(cadena: str, caracter: str) -> str:
      return caracter.join(cadena)

def sustituir_digitos( cadena: str, caracter: str) -> str:
    nueva_cadena = ""
    for letra in cadena:
        if letra.isdigit():
            nueva_cadena += caracter
        else:
            nueva_cadena += letra
    return nueva_cadena

def insertar_cada_tres_digitos(cadena: str, caracter: str) -> str:
    digitos = "".join(letra for letra in cadena if letra.isdigit())
    partes = []
    for i in range(0, len(digitos), 3):
        partes.append(digitos[i:i+3])
    return caracter.join(partes)

# pruebas
print(sustituir_espacios("Mi archivo txt", r"\_"))
print(insertar_entre_letras("separar", ","))
print(sustituir_digitos("su clave es: 1593", "X"))
print(insertar_cada_tres_digitos("ID: 99393922032932", "-"))

