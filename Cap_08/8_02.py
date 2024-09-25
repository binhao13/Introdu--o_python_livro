def multiplo(a,b):
    return a % b == 0
a = float(input("Digite um valor: "))
b = float(input("Digite um valor: "))
print(f"{a} é múltiplo de {b}: {multiplo(a,b)}")
