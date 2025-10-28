import math

def calcular_factorial_simple(m):
    print("\n--- CÁLCULO DE FACTORIALES ---")

    # Bucle para procesar m valores
    for i in range(1, m + 1):
        try:
            valor = int(input(f"Introduce el número {i} de {m}: "))

            # Usamos la función integrada de Python para calcular el factorial
            if valor < 0:
                resultado = "Error: Factorial no definido para negativos."
            else:
                resultado = math.factorial(valor)

            # Imprimir el resultado junto con el número de orden
            print(f"Orden {i}: El factorial de {valor} es {resultado}")

        except ValueError:
            print(f"Orden {i}: Error. Entrada inválida. Saltando este número.")

# --- Programa principal ---

try:
    m = int(input("Introduce la cantidad (m) de números a procesar: "))

    if m > 0:
        calcular_factorial_simple(m)
    else:
        print("La cantidad debe ser un número positivo.")

except ValueError:
    print("Error: La cantidad no es un número entero válido.")