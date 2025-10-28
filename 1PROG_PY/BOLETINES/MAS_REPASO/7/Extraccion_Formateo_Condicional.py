'''
Escribir unha función que reciba unha cadea de caracteres. Se a lonxitude da cadea é par, debe devolver
a primeira metade en minúsculas. Se a lonxitude é impar, debe devolver os últimos dous caracteres en maiúsculas.
'''
def formato_condicional(texto: str) -> str:
    lonxitude = len(texto)
    if lonxitude % 2 == 0:
        # Devolve a primeira metade en minúsculas
        metade = lonxitude // 2
        return texto[:metade].lower()
    else:
        # Devolve os dous últimos caracteres en maiúsculas
        return texto[-2:].upper()

print(formato_condicional("PythonPro"))
print(formato_condicional("Desenvolve"))
print(formato_condicional("DAM"))