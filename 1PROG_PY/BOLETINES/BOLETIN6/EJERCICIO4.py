def eliminar_asignaturas():

    asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

    asignaturasPendientes = []

    notas = []


    for i in range(len(asignaturas)): #recorrer la lista de asignaturas
        while True:
            try:
                entrada = input(f"Introduce la nota de la asignatura {i} : ")
                nota = int(entrada)

                notas.append(nota)

                if nota < 5:
                    asignaturasPendientes.append(asignaturas[i])

                break

            except ValueError:
                print("error")


    for asignatura, nota in zip(asignaturas, notas):
        print(f"En {asignatura} sacaste un {nota}")

    print("\n--- Asignaturas Pendientes (Suspensa) ---")
    if asignaturasPendientes:
        print((asignaturasPendientes))
    else:
        print("¡Felicidades! No tienes ninguna pendiente.")

if __name__ ==  "__main__":
    eliminar_asignaturas()