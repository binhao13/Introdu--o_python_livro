s1 = input("Digite uma string: ")
q = {}
x = 0
for letra in s1:
    if letra in q:
        q[letra] = q[letra] + 1    
    else:
        q[letra] = 1
for letra,valor in q.items():
    print(f"{letra}: {valor}x ")