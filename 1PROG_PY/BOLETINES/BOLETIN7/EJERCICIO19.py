def binario_a_decimal(cadea_binaria: str) -> int:
    return int(cadea_binaria, 2) #O 2 indica a base (binaria) na que se debe interpretar a cadea de caracteres.

# --- Exemplos de Uso ---
print(binario_a_decimal("101"))      # 5
print(binario_a_decimal("11111111")) # 255
print(binario_a_decimal("10101010")) # 170