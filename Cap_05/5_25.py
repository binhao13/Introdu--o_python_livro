n = int(input("Digite um número para se calcular a raiz: "))
b = 2
while abs(n -b**2) > 0.0001:
    p = (b+(n/b))/2
    b = p
print(f"Raiz = {p}")