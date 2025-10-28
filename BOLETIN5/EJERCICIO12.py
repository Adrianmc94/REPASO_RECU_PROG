def calcular_sueldos():

    #iniciamos los contadores
    rangoIndicado = 0
    menosIndicado = 0
    sueldo = -1

    while sueldo != 0:
        try:
            sueldo = float(input("Introduce el sueldo del trabajador: "))

            if sueldo < 0:
                print("introduce un sueldo mayor que 0.")
                continue # vuelve al inicio del bucle

            if sueldo < 999:
                menosIndicado += 1
                print(f"Trabajadores con un salario de menos de 1000€: {menosIndicado}")
            elif sueldo >= 1000 and sueldo <= 1750:
                rangoIndicado +=1
                print(f"Trabajadores con un salario dentro del rango: {rangoIndicado}")
            else:
                print("El trabajador cobra mas del rango indicado, bien por el")

        except ValueError:
            print("Erro: Introduce un número válido.")
            continue

if __name__ == "__main__":
    calcular_sueldos()

























