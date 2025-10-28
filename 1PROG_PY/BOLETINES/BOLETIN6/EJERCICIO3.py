

def numeros_inversos():

    numeros = []
    maximo = 10

    for i in range(maximo):
        entrada = input("Introduce los numeros del 1 al 10: ")
        numeroHastadiez = int(entrada)

        numeros.append(numeroHastadiez)
        numeros.sort(reverse=True)

    print(numeros)


if __name__ == "__main__":
    numeros_inversos()