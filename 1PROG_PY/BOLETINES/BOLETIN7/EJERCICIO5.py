#Conta as vocais e as consoantes do String “Python Python Python”. Ollo cos espazos!


texto = "Churruca Churruca Churruca"

vocales = "aeiou"
consonantes = "bcdfghjklmnpqrstvwxyz"

vocalesNum = 0
consonantesNum = 0

texto_minisculas = texto.lower() #pasamos la cadena a todo minusculas para trabajar mejor
texto_final = texto_minisculas.replace(" ", "") # sin espacios

for i in texto_final:
    if i in vocales:
        vocalesNum += 1
    elif i in consonantes:
        consonantesNum += 1

print(consonantesNum)
print(vocalesNum)


