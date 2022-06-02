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
p = a & b #Intersecção
n = b - a #Elementos exclusivos da 2° lista
r = a - b #Elementos que foram removidos da 2° lista
print(f""""Lista original: {l}
Lista modificada: {v}
Elementos que não mudaram: {p}
Os novos Elementos: {n}
Os elementos que foram removidos: {r}""")