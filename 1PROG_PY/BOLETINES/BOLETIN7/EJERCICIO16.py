def extraer_consoantes(cadea: str) -> str:
    vogais = "aeiouáéíóú"
    cadea_lower = cadea.lower()
    consoantes = [letra for letra in cadea_lower if letra.isalpha() and letra not in vogais]
    return "".join(consoantes)

def extraer_vogais(cadea: str) -> str:
    vogais = "aeiouáéíóú"
    cadea_lower = cadea.lower()
    vogais_atopadas = [letra for letra in cadea_lower if letra in vogais]
    return "".join(vogais_atopadas)

def substituir_vogais(cadea: str) -> str:
    mapa_substitucion = {
        'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a',
        'á': 'é', 'é': 'í', 'í': 'ó', 'ó': 'ú', 'ú': 'á',
        'ä': 'ë', 'ë': 'ï', 'ï': 'ö', 'ö': 'ü', 'ü': 'ä'
    }
    nova_cadea = []
    for letra in cadea:
        letra_lower = letra.lower()
        if letra_lower in mapa_substitucion:
            substituta = mapa_substitucion[letra_lower]
            # Manter a maiúscula se a orixinal era maiúscula
            if letra.isupper():
                nova_cadea.append(substituta.upper())
            else:
                nova_cadea.append(substituta)
        else:
            nova_cadea.append(letra)
    return "".join(nova_cadea)

# --- Exemplos de Uso ---
print(extraer_consoantes('algoritmos'))
print(extraer_vogais('sen consonantes'))
print(substituir_vogais('vestiario'))