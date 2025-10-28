def suma_numeros():

    numerosSolicitados = 0
    sumaTotal = 0
    limiteNumeros = 10
    limiteTotal = 999

    while numerosSolicitados < limiteNumeros:
        try:
            entrada = input("Introduce un numero: ")
            numero = int(entrada)

            if numero == limiteTotal:
                print("programa detenido")
                break

            sumaTotal += numero
            numerosSolicitados += 1
        except ValueError:
            print("error")

    print("RESULTADO")
    print(f"La suma total de numeros es de: {sumaTotal}")
    print(f"Numeros solicitados: {numerosSolicitados}")


if __name__ == "__main__":
    suma_numeros()