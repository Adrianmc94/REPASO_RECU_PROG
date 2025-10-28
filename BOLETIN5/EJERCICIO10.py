def calculoArea(base, altura):

    area = base * altura
    return area

while True:
     try:
        altura = float(input("Dime la altura del rectangulo YA: "))
        base = float(input("Dime la base YA: "))
        resultado = calculoArea(base, altura)
        print(f"El area del rectaguno es de :{resultado}")
        break

     except ValueError:
         print("Introduce un numero valido parvo")
