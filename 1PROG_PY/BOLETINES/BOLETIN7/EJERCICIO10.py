#Tenta escribir un método, que dado un obxecto da clase str conte diferentes tipos de caracteres.
#En particular, o método deberá imprimir o número de letras, díxitos e espazos en branco da cadea.
#Tenta facer un programa que escriba o cálculo da cadea: «Ola, son alumno de DAM1, e son programador desde o 2025».
class AnalizadorCadena:

    @staticmethod
    def contar_caracteres(cadena: str):
        letras = 0
        digitos = 0
        espacios = 0

        for i in cadena:
            if i.isalpha():
                letras += 1
            elif i.isdigit():
                digitos += 1
            elif i.isspace():
                espacios += 1

        print(f"Número de LETRAS: {letras}")
        print(f"Número de DÍXITOS: {digitos}")
        print(f"Número de ESPAZOS: {espacios}")


texto = "dmdn  dwqkdnQD 4I4 DNQWDBNQW2922 DMNWDW2"


AnalizadorCadena.contar_caracteres(texto)



