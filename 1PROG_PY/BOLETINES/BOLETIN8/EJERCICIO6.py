'''
Dada unha lista de números enteiros, escribir unha función que:
Devolte unha lista con tódolos que sexan primos.
Devolte o sumatorio e o promedio dos valores.
Devolte unha lista co factorial de cada un de eses números.
'''
import math

def filtrar_primos(lista_numeros: list) -> list:
    primos = []
    for numero in lista_numeros:
        if numero > 1:
            e_primo = True
            for i in range(2, int(math.sqrt(numero)) + 1):
                if numero % i == 0:
                    e_primo = False
                    break
            if e_primo:
                primos.append(numero)
    return primos

def sumar_e_promediar(lista_numeros: list) -> tuple:
    if not lista_numeros:
        return (0, 0.0)

    sumatorio = sum(lista_numeros)
    promedio = sumatorio / len(lista_numeros)
    return (sumatorio, promedio)

def calcular_factoriais(lista_numeros: list) -> list:
    factoriais = []
    for numero in lista_numeros:
        if numero >= 0:
            factoriais.append(math.factorial(numero))
        else:
            factoriais.append(None)
    return factoriais

numeros = [1, 2, 3, 4, 5, 6, 7, 10, 11]

primos = filtrar_primos(numeros)
print(f"Primos: {primos}")

suma, promedio = sumar_e_promediar(numeros)
print(f"Suma: {suma}, Promedio: {promedio}")

factoriais = calcular_factoriais(numeros)
print(f"Factoriais: {factoriais}")