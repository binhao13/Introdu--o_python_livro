k = float(input("Digite a quantidade de kilometros percorridos: "))
d = float(input("Digite a quantidade de dias: "))
p = d*60 + 0.15*k
print(f"O preço a se pagar é: R${p:.2f}")