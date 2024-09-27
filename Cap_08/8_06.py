def soma(l):
    total = 0
    for e in l:
        total += e
    return total

l =[]
x = 0
while True:
    n = (input("Digite um número (00 para sair): "))
    if n == '00':
        break
    else:
        n = int(n)
        l.append(n)
        x+=1
print(l)
print(soma(l))