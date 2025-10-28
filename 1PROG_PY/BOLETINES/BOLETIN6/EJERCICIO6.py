def palindormo():
     entrada = input("Introduce una palabra: ")


     #Ponemos la palabras en minisculas y sin espacios para trabajar con ella mejor

     palabraProcesada = entrada.lower().replace(" ", "")

     #Obtenemos la palabra invera para comparar
     palabraInversa = palabraProcesada[::-1]

     if entrada == palabraInversa:
         print("si es un palindormo de eses bro")
     else:
         print("no lo es bro")


if __name__ == "__main__":
    palindormo()