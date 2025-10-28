def formatear_numero_miles(numeroSTR: str) -> str:

    try:
        return f"{int(numeroSTR):,}".replace(",", ".")
    except ValueError:
        return "error"

print(formatear_numero_miles("1234567898"))