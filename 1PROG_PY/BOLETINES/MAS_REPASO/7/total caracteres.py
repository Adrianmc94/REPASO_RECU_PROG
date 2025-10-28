'''
Escribir unha función que reciba unha cadea e devolva o número total de caracteres
que non son nin vogais (inclúe acentuadas), nin díxitos, nin espazos en branco.
'''
def contar_non_vogais_non_dixitos(cadea: str) -> int:
    vogais = "aeiouáéíóú"
    contador = 0

    for caracter in cadea:
        # Ignoramos explícitamente os espazos
        if caracter.isspace():
            continue

        caracter_lower = caracter.lower()

        # Se non é vogal E non é díxito
        if caracter_lower not in vogais and not caracter.isdigit():
            contador += 1

    return contador

print(contar_non_vogais_non_dixitos("DAM1 - A Coruña 2024!"))