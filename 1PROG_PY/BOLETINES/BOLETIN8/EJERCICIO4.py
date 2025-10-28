'''
Escribir unha función que reciba unha tupla con nomes,
unha posición de orixen p e unha cantidade n, e imprima a mensaxe anterior
(exercicio 3) para os n nombres que se encontran a partires da posición p.
'''

def saudar_nomes_rango(nomes: tuple, p: int, n: int):
    if p < 0 or p >= len(nomes) or n <= 0:
        return

    nomes_a_saudar = nomes[p : p + n]

    for nome in nomes_a_saudar:
        print(f"Estimado don/dona {nome}")

nomes_lista = ("Xoan", "Maria", "Antón", "Laura", "Pedro", "Sofia")

print("--- Test 1 (Inicio en 1, Cantidade 3) ---")
saudar_nomes_rango(nomes_lista, 1, 3)

print("\n--- Test 2 (Inicio en 3, Cantidade 4 - Trunca) ---")
saudar_nomes_rango(nomes_lista, 3, 4)

print("\n--- Test 3 (Inicio en 0, Cantidade 1) ---")
saudar_nomes_rango(nomes_lista, 0, 1)