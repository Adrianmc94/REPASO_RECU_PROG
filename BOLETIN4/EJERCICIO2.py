print("--CALCULAR SUPERFICIE DE FIGURAS--")
print("1...Cuadrado")
print("2...Triangulo")
print("3...Circulo")

eleccion = int(input("Que figura eligues perro?: "))

eleccion = eleccion

match eleccion:
    case 1:
        lado = int(input("Introduce la longitud del lado del cuadrado: "))

        resultado = lado * lado
        print(f"La superficie del cuadrado es de {resultado} metros cuadrados")

    case 2:
        base = int(input("Introduce la base del triangulo: "))
        altura = int(input("Introduce la altura del triangulo: "))

        resultado = (base * altura) / 2
        print(f"La superficie del triangulo es de {resultado} metros cuadrados")

    case 3:
        radio = int(input("Introduce el radio del circulo: "))

        resultado = 3.14159 * (radio ** 2)
        print(f"La superficie del circulo es de {resultado:.2f} metros cuadrados")

    case _:
        print("La opción elegida no es válida.")