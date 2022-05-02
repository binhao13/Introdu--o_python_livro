l = []
v = []
t = []
print("-------------Lista 1-------------")
while True:
    n = float(input("Digite um número (0 para sair): "))
    if n == 0:
        break
    l.append(n)
t.extend(l)
print("-------------Lista 2-------------")
while True:
    q = float(input("Digite um número (0 para sair): "))
    if q == 0:
        break
    else:
        v.append(q)
        x = 0
        z = 0
        while z < len(t):
            if q == t[z]:
                x += 1 
                z += 1
                break
            else:
                z += 1
        if x == 0:
            t.append(q)

print("---------------------------------")
print(f"""Lista 1: {l}
Lista 2: {v}
Lista 3: {t} """)