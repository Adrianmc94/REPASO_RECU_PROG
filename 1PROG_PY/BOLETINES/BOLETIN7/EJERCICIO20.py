def crear_cadea_lonxitude(cadea_orixe: str, caracter_novo: str) -> str:
    lonxitude = len(cadea_orixe)
    return caracter_novo * lonxitude

def marcar_caracter(cadea_orixe: str, caracter_a_buscar: str) -> str:
    resultado = ""
    for letra in cadea_orixe:
        if letra == caracter_a_buscar:
            resultado += caracter_a_buscar
        else:
            resultado += "-"
    return resultado

# --- Exemplos de Uso ---
print(crear_cadea_lonxitude('algoritmos', '*'))
print(marcar_caracter('banana', 'a'))
print(marcar_caracter('algoritmos', 'o'))