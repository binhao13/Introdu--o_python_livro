x = float(input("Digite a quantidade de energia(Kwh) consumida: "))
i = input("Digite o tipo de instalação da sua casa \nR = residências || \
C = comércios || I = indústrias: ")
if i == "c":
    if x <= 500:
        p = 0.4*x
    else:
        p = 0.65*x
elif i == "r":
    if x <= 1000:
        p = 0.55*x
    else:
        p = 0.6*x
elif i == "i":
    if x <= 5000:
        p = 0.55*x
    else:
        p = 0.6*x
print(f"O valor a pagar é R${p:.2f}")       