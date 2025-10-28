def notas_asignaturas():

    asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

    notas = []

    for asignatura in asignaturas:
        while True:
            try:
                nota = float(input(f"Introduce la nota de: {asignatura} "))

                if nota >=0 and nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("error")

            except ValueError:
                print("error error")

    #mostramos resultados
    for asignatura, nota in zip(asignaturas, notas):
        print(f"En {asignatura} sacaste un {nota}")


if __name__ == "__main__":
    notas_asignaturas()