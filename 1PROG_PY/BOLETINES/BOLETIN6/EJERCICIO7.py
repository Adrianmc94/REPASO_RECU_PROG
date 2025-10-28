def contarVocales():

    entrada = input("Introduce una palabra: ")

    palabraMinusculas = entrada.lower()

    vocales = ['a', 'e', 'i', 'o', 'u']

    #Diccionario para almacenar resultados
    conteoVocales = {}

    #Iniciar el diccionario a 0
    for vocal in vocales:
        conteoVocales[vocal] = 0

    #Contar las vocales de la palabra
    for letra in palabraMinusculas:
        if letra in vocales:
            conteoVocales[letra] += 1


    for vocal, conta in conteoVocales.items():
        print(f"La vocal {vocal} aparece {conta} veces")


if __name__ == "__main__":
    contarVocales()















if __name__ == "__main__":
    contarVocales()