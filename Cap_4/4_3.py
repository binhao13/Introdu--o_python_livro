x = []
e = 0
while e < 3:
    n = float(input("Digite um número: "))
    x.append(n)
    e+=1
fim = 3
while fim > 1:
    trocou = False
    e = 0
    while e < fim - 1:
        if x[e] > x[e + 1]:
            trocou  = True
            temp = x[e]
            x[e] = x[e + 1]
            x[e + 1] = temp
        e+=1
    if not trocou:
        break
    fim-=1    
            
print(f"Maior: {x[2]} e Menor: {x[0]}")
        