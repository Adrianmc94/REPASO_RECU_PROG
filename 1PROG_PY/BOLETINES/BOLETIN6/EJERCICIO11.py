import statistics

def calcular_est():

    entrada = input("Números (separados por comas): ")

    try:
        # Garda os números nunha lista (list of floats)
        numeros = [float(n.strip()) for n in entrada.split(',')]

    except ValueError:
        print("Erro: Entrada non válida.")
        return

    n = len(numeros)

    if n < 1:
        print("Erro: Non se introduciu ningún dato.")
        return

    # Calcula a media
    media = statistics.mean(numeros)

    # Comproba se se pode calcular a desviación típica
    if n < 2:
        desviacion_tipica = "Non aplicable (menos de 2 datos)"
    else:
        # Desviación típica AMOS TRAL
        desviacion_tipica = statistics.stdev(numeros)

    # Mostra os resultados
    print(f"\nMedia: {media:.4f}")

    if isinstance(desviacion_tipica, float):
        print(f"Desviación Típica: {desviacion_tipica:.4f}")
    else:
        print(f"Desviación Típica: {desviacion_tipica}")

calcular_est()