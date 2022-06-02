s = "AABBEFAATT"
s2 = "BE"
p = 0
p = s.find(s2,p)
if p >= 0:
    print(f"{s2} encontrado na posição {p} de {s}")
else:
    print("Não encontrado")  