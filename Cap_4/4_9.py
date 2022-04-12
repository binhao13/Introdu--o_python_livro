v = float(input("Digite o valor da casa: "))
s = float(input("Digite o seu salário: "))
a = float(input("Digite a quantidade de anos a pagar: "))
p = v/(a*12)
if p > 0.3*s:
    print("A compra não pode ser feita com seu salário atual")
else:
    print(f"O valor da prestação será de R${p:.2f}")

