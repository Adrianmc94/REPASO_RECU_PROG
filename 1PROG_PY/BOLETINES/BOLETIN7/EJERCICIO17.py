def verificar_palindromo_simple(cadea: str) -> bool:
    cadea_limpa = cadea.lower().replace(' ', '')
    return cadea_limpa == cadea_limpa[::-1]

# --- Exemplos de Uso ---
print(verificar_palindromo_simple('anita lava la tina'))
print(verificar_palindromo_simple('Somos'))
print(verificar_palindromo_simple('A mala alma'))
print(verificar_palindromo_simple('test'))