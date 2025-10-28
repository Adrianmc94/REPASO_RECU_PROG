def comprobar_subcadea(cadea_principal: str, subcadea: str) -> bool:
    return subcadea in cadea_principal

def anterior_alfabetico(cadea1: str, cadea2: str) -> str:
    if cadea1 < cadea2:
        return cadea1
    else:
        return cadea2

# --- Exemplos de Uso ---
print(comprobar_subcadea('subcadea', 'cadea'))
print(comprobar_subcadea('python', 'java'))
print(anterior_alfabetico('kde', 'gnome'))
print(anterior_alfabetico('apple', 'banana'))