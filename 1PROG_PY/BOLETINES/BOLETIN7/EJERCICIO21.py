def validar_contrasinal(contrasinal: str) -> bool:
    if len(contrasinal) < 8:
        return False

    ten_maiuscula = any(c.isupper() for c in contrasinal)
    ten_minuscula = any(c.islower() for c in contrasinal)
    ten_numero = any(c.isdigit() for c in contrasinal)

    return ten_maiuscula and ten_minuscula and ten_numero

# --- Exemplos de Uso ---
print(validar_contrasinal("Contrasinal123")) # True
print(validar_contrasinal("curto8"))        # False (Menos de 8)
print(validar_contrasinal("senmaiuscula1")) # False (Non ten maiúscula)
print(validar_contrasinal("SOLOENMAIUSCULAS1")) # False (Non ten minúscula)
print(validar_contrasinal("senumero"))      # False (Non ten número)