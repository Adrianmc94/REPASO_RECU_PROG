def fahrenheit_a_celsius(fahrenheit):
    """Realiza a conversión de temperatura de Fahrenheit a Celsius."""
    # Despexamos a fórmula: C = 5/9 * (F - 32)
    # É crucial usar 5.0 ou 9.0 para asegurar a división flotante en Python
    celsius = (fahrenheit - 32) * (5.0 / 9.0)
    return celsius

# --- Programa principal ---

while True:
    try:
        temp_f = float(input("Introduce a temperatura en graos Fahrenheit (°F): "))

        # Realizamos a conversión
        temp_c = fahrenheit_a_celsius(temp_f)

        print(f"\n{temp_f}°F equivalen a {temp_c:.2f}°C")
        break

    except ValueError:
        print("Erro: A entrada non é un número válido. Por favor, introduce un valor numérico.")