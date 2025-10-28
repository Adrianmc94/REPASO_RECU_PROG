def dibujar_arbol():

    while True:
        try:
            numero = int(input("Introduce la altura que quieres q tenga el arbol: "))

            if numero < 0:
                print("Pon un numero mayor que 0 hombre")
            else:
                #Iniciamos el bucle q dibujara el triangulo
                for i in range (1, numero + 1):
                    espacios = " " * (numero - i)

                    simbolos = "* " * i

                    lineaImprimir = simbolos[:-1]

                    print(espacios + lineaImprimir)

                break # Saímos do bucle 'while' despois de debuxar

        except ValueError:
            print("Entrada non válida. Por favor, introduce un número enteiro.")

if __name__ == "__main__":
    dibujar_arbol()