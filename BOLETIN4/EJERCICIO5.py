def calcular_letra_dni(numero_dni):
    letras_dni = 'TRWAGMYFPDXBNJZSQVHLCKE'

    resto = numero_dni % 23

    letra = letras_dni[resto]

    return letra

while True:
    try:
        entrada_dni = input("Introduce el número de DNI (sin letra): ")

        numero_dni = int(entrada_dni)

        if len(entrada_dni) != 8:
            print("Aviso: El DNI estándar tiene 8 dígitos. El cálculo se realizará igualmente.")

        letra_resultante = calcular_letra_dni(numero_dni)

        print(f"El número introducido es: {numero_dni}")
        print(f"El resto de la división por 23 es: {numero_dni % 23}")
        print(f"La letra del DNI correspondiente es: {letra_resultante}")
        print(f"DNI completo: {numero_dni}{letra_resultante}")

        break

    except ValueError:
        print("Error: La entrada no es un número entero válido. Inténtalo de nuevo.")