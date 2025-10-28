def numeros_ganadores():

    numerosGanadores = []
    numeroDeNumeros = 6

    for i in range(numeroDeNumeros):
        while True:
            try:
                entrada = input("Introduce o número gañador: ")
                numero = int(entrada)
                numerosGanadores.append(numero)
                break
            except ValueError:
                print("Erro: introduce un número enteiro.")

    numerosGanadores.sort()   #para ordenador de menor a mayor, si fuera de mayor a menos seria: numerosGanadores.sort(reverse=True)

    print("\nOs números gañadores ordenados son:")
    print(numerosGanadores)


if __name__ == "__main__":
    numeros_ganadores()