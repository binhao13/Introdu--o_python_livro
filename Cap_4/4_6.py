d = float(input("Digite a distância que você deseja percorrer (km): "))
if d <= 250:
    p = 0.5*d
else:
    p = 0.45*d
print(f"O preço da passagem é R${p:.2f}")
