'''
Enunciado: Escribir una función que reciba una cadena principal y una subcadena de búsqueda, y devuelva
True solo si la subcadena está presente en la principal Y es un palíndromo (ignorando mayúsculas, minúsculas y espacios).
'''
def verificar_subcadea_palindromo(cadea: str, subcadea: str) -> bool:

    def e_palindromo(s):
        s_limpa = "".join(c for c in s if c.isalpha()).lower()
        return s_limpa == s_limpa[::-1]

    if subcadea not in cadea:
        return False

    return e_palindromo(subcadea)

print(verificar_subcadea_palindromo("Este texto contén radar de alerta", "radar"))
print(verificar_subcadea_palindromo("Este texto contén radar", "alerta"))
print(verificar_subcadea_palindromo("Ola mundo", "Ola"))