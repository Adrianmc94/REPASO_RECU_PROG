def siglas_palabras(cadena: str) -> str:
    palabras = cadena.split()
    primeras_letras = [palabra[0].upper() for palabra in palabras if palabra]
    return "".join(primeras_letras)

def capitalizar_palabras(cadena: str) -> str:
    return cadena.title()

def palabras_con_a(cadena: str) -> str:
    palabras = cadena.split()
    palabras_filtradas = []
    for palabra in palabras:
        if palabra and palabra[0].upper() == "A":
            palabras_filtradas.append(palabra)
    return " ".join(palabras_filtradas)

print(siglas_palabras("Universal Serial Bus"))
print(capitalizar_palabras("republica argentina"))
print(palabras_con_a("Antes de abrir"))