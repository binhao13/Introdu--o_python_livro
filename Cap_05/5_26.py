n = int(input("Digite um número: "))
d = int(input("Digite outro número: "))

while n >= d:
    n -= d
print(f"O resto da divisão é igual a {n}")