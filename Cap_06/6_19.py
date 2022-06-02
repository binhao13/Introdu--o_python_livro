l = []
v = []
while True:
    x = input("Digite um elemento para a primeira lista(fim para sair): ")
    if x == "fim":
        break
    else:
        l.append(x)
while True:
    y = input("Digite um elemento para a segunda lista(fim para sair): ")
    if y == "fim":
        break
    else:
        v.append(y)
a = set(l)
b = set(v)
c = a - b #Valores q só tem na 1° lista
d = b - a #Valores q só tem na 2° lista
e = a|b #lista com os elementos não repetidos das duas listas
f = e - d - c #Valores comuns as duas listas
print(f"""Valores comuns as duas listas {f}
Valores que só existem na 1° lista {c}
Valores que só existem na 2° lista {d}
Lista com os elementos não repetidos das duas listas {e}
Primeira lista, sem os elementos repetidos na segunda {c}""")

