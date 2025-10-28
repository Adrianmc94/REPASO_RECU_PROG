'''
Pregado de un texto. Escribir unha función que reciba un texto e unha lonxitude e devolva
unha lista de cadeas de como máximo esa lonxitude. As líñas deben cortarse correctamente nos espazos (sen cortar as palabras).
'''
def axustar_texto(texto: str, lonxitude_max: int) -> list:
    palabras = texto.split()
    if not palabras:
        return []

    liñas = []
    liña_actual = ""

    for palabra in palabras:
        if not liña_actual:
            liña_actual = palabra
        elif len(liña_actual) + 1 + len(palabra) <= lonxitude_max:
            liña_actual += " " + palabra
        else:
            liñas.append(liña_actual)
            liña_actual = palabra

    if liña_actual:
        liñas.append(liña_actual)

    return liñas

texto_exemplo = "Esta é unha cadea de texto moi longa que necesitamos axustar a un ancho fixo."
ancho = 20
resultado = axustar_texto(texto_exemplo, ancho)
print(resultado)