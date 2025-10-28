from lib2to3.fixer_util import String

nombrePrimeraPerosona = input("Nombre de la persona 1: ")
pesoPrimeraPersona = int(input("Peso de la primera persona: "))

nombreSegundaPerosona = input("Nombre de la persona 2: ")
pesoSegundaPersona = int(input("Peso de la segunda persona: "))


if pesoPrimeraPersona > pesoSegundaPersona:
    diferenciaPeso = pesoPrimeraPersona - pesoSegundaPersona
    print(f"{nombrePrimeraPerosona} es mas pesado que {nombreSegundaPerosona}")
    print(f"La diferencia del peso es de: {diferenciaPeso}")

elif pesoPrimeraPersona < pesoSegundaPersona:
    diferenciaPeso2 = pesoSegundaPersona - pesoPrimeraPersona
    print(f"{nombreSegundaPerosona} es mas pesado que {nombrePrimeraPerosona}")
    print(f"La diferencia del peso es de: {diferenciaPeso2}")