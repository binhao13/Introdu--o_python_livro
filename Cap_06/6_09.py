from operator import truediv


l = [15,7,27,39]
p = int(input("Digite o valor a procurar: "))
v = int(input("Digite outro valor a procurar: "))
x = 0
y = 0
achou1 = False
achou2 = False
while x < len(l):
    if l[x] == p:
        print(f"{p} achado na posição {x}")
        achou1 = True
    elif l[x] == v:
        print(f"{v} achado na posição {x}")
        achou2 = True
    elif achou1 and achou2:
        break
    x += 1
if achou1 == False:
    print(f"{p} não encontrado")
if achou2 == False:
    print(f"{v} não encontrado")