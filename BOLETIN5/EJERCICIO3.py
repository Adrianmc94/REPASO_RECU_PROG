def conversion(fahrenheit):

    celsius = (fahrenheit - 32) * (5.0 / 9.0)
    return celsius

# --- Programa principal ---

print("--- TÁBOA DE CONVERSIÓN DE TEMPERATURAS ---")
print("| Fahrenheit (°F) | Celsius (°C) |")
print("|-----------------|--------------|")

#bucle
for rangoF in range (1, 121, 10):
    gradosC = conversion(rangoF) #calculamos llamando al metodo de arriba

    print(f"| {str(rangoF).ljust(15)} | {gradosC:.2f} |")