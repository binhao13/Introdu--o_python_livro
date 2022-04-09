s = float(input("Digite seu salário: "))
if s > 1250:
    a = 0.1*s
else:
    a = 0.15*s
print(f"O aumento é de R$ {a:.2f}")