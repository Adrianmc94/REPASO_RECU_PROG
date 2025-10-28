'''
Escribir unha función que reciba unha tupla con nomes
e para cada nome imprima unha mensaxe ‘Estimado don/dona Nome’
'''
def saudar_nomes(nomes: tuple):
    for nome in nomes:
        # Usamos 'don'/'dona' como marcador xenérico, como suxire o enunciado
        print(f"Estimado don/dona {nome}")

# --- Exemplos de Uso ---
saudar_nomes(("Xoan", "Maria", "Antón"))