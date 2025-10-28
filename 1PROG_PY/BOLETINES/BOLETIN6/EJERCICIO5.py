import string

def filtrar_abecedario():

    abecedario = list(string.ascii_lowercase)

    abecedario_filtrado = []

    for i in range(len(abecedario)):

        indice_real = i + 1 

        if i % 3 != 0:
            abecedario_filtrado.append(abecedario[i])

    print(abecedario_filtrado)

if __name__ == "__main__":
    filtrar_abecedario()