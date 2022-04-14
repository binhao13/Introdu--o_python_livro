di = float(input("Digite o depósito inicial: "))
txj = float(input("Digite a taxa de juros: "))
m = 24
i = 0
df = di
ap = float(input("Digite seu aporte mensal: "))
while i <= m:
    txjp = txj/100
    df =  (df + ap)*(txjp + 1)
    print(f"Saldo do mês: R${df:.2f}")
    i += 1
ac = df - di
print(f"O ganho total com juos foi de: R${ac:.2f}")