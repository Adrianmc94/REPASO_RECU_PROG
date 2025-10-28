'''
Enunciado: Escribir una función que reciba una lista de enteros y un valor de corte C. La función debe devolver un diccionario que separe los números en dos listas: aquellos
menores que C y los factoriales de aquellos mayores o iguales que C (asumiendo math.factorial).
'''
import math

def filtrar_e_operar(lista_numeros: list, C: int) -> dict:
    menores_que_C = [n for n in lista_numeros if n < C]

    factoriais_maiores_ou_iguais = []
    for n in lista_numeros:
        if n >= C and n >= 0:
            factoriais_maiores_ou_iguais.append(math.factorial(n))
        elif n >= C and n < 0:
            factoriais_maiores_ou_iguais.append(None)

    return {
        "menores_que_C": menores_que_C,
        "factoriais_maiores_ou_iguais": factoriais_maiores_ou_iguais
    }

print(filtrar_e_operar([3, 5, 0, 7, 2, 4], 4))