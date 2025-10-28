'''
Modificar as funcións anteriores para que teñan en conta o xénero do destinatario, para elo, deberán recibir unha tupla de tuplas,
contendo o nome e o xénero, adaptando a mensaxe con ‘don’ ou ‘dona’ dependendo deste.
'''

def saudar_nomes_rango_xenero(persoas: tuple, p: int, n: int):
    if p < 0 or p >= len(persoas) or n <= 0:
        return

    persoas_a_saudar = persoas[p : p + n]

    for persoa in persoas_a_saudar:
        nome = persoa[0]
        xenero = persoa[1].upper()

        if xenero == 'F':
            tratamento = "dona"
        else:
            tratamento = "don"

        print(f"Estimado/a {tratamento} {nome}")

persoas_lista = (
    ("Xoan", "M"),
    ("Maria", "F"),
    ("Antón", "M"),
    ("Laura", "F"),
    ("Pedro", "M"),
    ("Sofia", "F")
)

print("--- Test 1 (Inicio en 1, Cantidade 3) ---")
saudar_nomes_rango_xenero(persoas_lista, 1, 3)

print("\n--- Test 2 (Inicio en 0, Cantidade 2) ---")
saudar_nomes_rango_xenero(persoas_lista, 0, 2)