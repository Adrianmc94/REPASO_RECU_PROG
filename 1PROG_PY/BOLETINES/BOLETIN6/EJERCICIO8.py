def almacen_listas():

    lista = [50, 75, 46, 22, 80, 65, 8]

    precioMenor = min(lista)
    # CORRIXIDO: Usar f-string e a palabra "menor"
    print(f"{precioMenor} es el precio menor")

    precioMayor = max(lista)
    print(f"{precioMayor} es el precip mayor")

if __name__ == "__main__":
    almacen_listas()