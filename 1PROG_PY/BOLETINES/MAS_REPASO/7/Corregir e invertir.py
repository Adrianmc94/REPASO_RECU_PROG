'''
Escribir unha función que reciba unha cadea de texto e un enteiro N.
Se a cadea contén a subcadea "error" (ignorando maiúsculas/minúsculas),
debe devolver a cadea coa subcadea "error" substituída por N.
Se non a contén, debe devolver a cadea orixinal invertida.
'''
def corrixir_e_inverter(texto: str, N: int) -> str:
    subcadea_error = "error"
    if subcadea_error in texto.lower():
        # Substitúe as posibles variantes de "error" por N
        texto = texto.replace(subcadea_error, str(N)).replace(subcadea_error.capitalize(), str(N)).replace(subcadea_error.upper(), str(N))
        return texto
    else:
        # Invierte a cadea
        return texto[::-1]

print(corrixir_e_inverter("Ocorreu un error grave.", 500))
print(corrixir_e_inverter("Todo funcionou ben.", 200))