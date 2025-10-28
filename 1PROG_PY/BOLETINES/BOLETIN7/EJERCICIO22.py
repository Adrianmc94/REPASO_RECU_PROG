def formatear_nome(nome_completo: str) -> str:
    partes = nome_completo.split()

    nome_formateado = ""
    for parte in partes:
        if parte:
            # Capitaliza a primeira letra e engade o resto da palabra
            nome_formateado += parte[0].upper() + parte[1:].lower() + " "

    return nome_formateado.strip()

# --- Exemplos de Uso ---
print(formatear_nome("juan perez garcia"))
print(formatear_nome("MARIA lopez"))
print(formatear_nome("   ana marta   "))