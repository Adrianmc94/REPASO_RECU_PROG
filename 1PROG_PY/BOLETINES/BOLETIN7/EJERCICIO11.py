#Escribir funcións que dada unha cadena de caracteres:
#Imprima os dous primeiros caracteres.
#Imprima os tres últimos caracteres.
#Imprima dita cadea cada dous caracteres. Ex.: recta debería imprimir rca
#Imprima a cadea nun sentido e en sentido inverso. Ex: reflexo imprime reflexooxelfer.

class funciones:

    @staticmethod
    def dos_primeros_numeros(texto: str):
        dos_primeros = texto[0:2]
        print(dos_primeros)
    @staticmethod
    def tres_ultimos(texto: str):
        tres_ultimos = texto[-3:]
        print(tres_ultimos)
    @staticmethod
    def cada_dos(texto: str):
        cada_dos_c = texto[::2]
        print(cada_dos_c)
    @staticmethod
    def sentidos(texto: str):
        sentido_orign = texto
        print(f"Texro original: {texto}")

        sentido_inverso = texto[::-1]
        print(f"Texto inverso: {sentido_inverso}")


texto_prueba = "bomba esto es una prueba"

funciones.dos_primeros_numeros(texto_prueba)
funciones.tres_ultimos(texto_prueba)
funciones.cada_dos(texto_prueba)
funciones.sentidos(texto_prueba)