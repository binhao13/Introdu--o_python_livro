s = 0
i = 0
while True:
    n = int(input("Digite um número (0 para parar): "))
    if n == 0:
        break
    i += 1
    s = s + n
m = s/i
print("-----------------------------------------")
print(f"Quantidade de números digitados: {i}\n\
Soma = {s}\n\
Média = {m}")