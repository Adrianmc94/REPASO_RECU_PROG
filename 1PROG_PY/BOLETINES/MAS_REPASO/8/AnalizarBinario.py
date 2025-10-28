'''
Escribir una función que reciba una cadena binaria ("11010") y devuelva una tupla que contenga su valor decimal y un
booleano indicando si tiene un número par de dígitos '1'.
'''
def analizar_binario(cadea_binaria: str) -> tuple:
    decimal = int(cadea_binaria, 2)
    par_uns = cadea_binaria.count('1') % 2 == 0
    return (decimal, par_uns)

print(analizar_binario("11010"))