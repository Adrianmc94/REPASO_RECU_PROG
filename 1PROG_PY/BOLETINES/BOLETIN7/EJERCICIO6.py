#Divide a cadea de texto “ www. phytonparatodos. com” en duas partes
#“ www. phyton” e “paratodos. com”. Para posteriormente concaténalas e mostralas de novo

texto = " www. churruca .com"

#dividimos la cadena
parte1 = texto[:4]   # pilla desde el principio hasta el indice 4 en este caso
parte2 = texto[8:]   #pilla desde el indice 8 hasta el final

texto_comcatenado = parte1 + parte2

print(texto_comcatenado)
