numeros = [1,3,5,-3,-6,39,0,5,-2,0]

negativos = 0
positivos = 0
ceros = 0

for numero in numeros:

    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1
    else:
        ceros +=1
print("---NUMEROS---")
print(f"Negativos: {negativos}")
print(f"Positivos {positivos}")
print(f"Ceros: {ceros}")


