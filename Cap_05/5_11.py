di = float(input("Digite o depósito inicial: "))
txj = float(input("Digite a taxa de juros: "))
m = 24
i = 0
df = di
while i <= m:
    txjp = txj/100
    df =  df*(txjp + 1)
    print(f"Saldo do mês: R${df:.2f}")
    i += 1
ac = df - di
print(f"O ganho total com juros foi de: R${ac:.2f}")