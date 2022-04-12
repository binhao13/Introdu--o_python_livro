p = float(input("Digite o preço do produto: "))
d = float(input("Digite o percentual de desconto: "))
des = p*(d/100)
pre = p - des
print(f"O desconto é de: R${des:.2f}")
print(f"O preço é de: R${pre:.2f}")