def imprimir_taboa_multiplicar(numero):

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    print("------------------------")

while True:
    try:
        numero = int(input("Pon un numero y callate: "))

        if numero == 0:
            print("saliendo, q te vaya bien")
            break

        imprimir_taboa_multiplicar(numero)

    except ValueError:
        print("bro pon un numero bro q sea valido bro")