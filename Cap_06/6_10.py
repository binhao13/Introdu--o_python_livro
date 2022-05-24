l = [15,7,27,39]
p = int(input("Digite o valor a procurar: "))
v = int(input("Digite outro valor a procurar: "))
x = 0
y = 0
z = 0
achou1 = False
achou2 = False
while x < len(l):
    if l[x] == p:
        print(f"{p} achado na posição {x}")
        achou1 = True
        y = x
    elif l[x] == v:
        print(f"{v} achado na posição {x}")
        achou2 = True
        z = x
    elif achou1 and achou2:
        break
    x += 1
if achou1 == False:
    print(f"{p} não encontrado")
elif achou2 == False:
    print(f"{v} não encontrado")
if y < z:
    print(f"p foi achado primeiro")
else:
    print(f"v foi achado primeiro")