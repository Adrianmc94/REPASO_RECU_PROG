

numero = int(input("Introduce un numeor entero: " ))

#Manera larga pero facil de hacerlo
'''
if numero > 0:
    print(f"El valor absoluto de {numero} es {numero}")
elif numero < 0:
    resultado = numero * -1
    print(f"El valor absoluto de {numero} es {resultado}")
else:
    print("el numero es 0 mi loco")
'''

#Manera corta pero algo mas chungo:
valor_absoluto = numero * -1 if numero < 0 else numero

print(f"El valor absoluto de {numero} es {valor_absoluto}")

