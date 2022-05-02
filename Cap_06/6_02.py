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
    v.append(q)
t.extend(v)
print("---------------------------------")
print(f"""Lista 1: {l}
Lista 2: {v}
Lista 3: {t} """)