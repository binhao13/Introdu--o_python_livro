t = 0
while True:
    n = int(input("Digite o código do produto (0 para sair): "))
    if n == 0:
        break
    q = int(input("Digite a quantidade comprada do produto cujo o código foi selecionado:"))
    if n == 1:
        p = 0.5
        
    elif n == 2:
        p = 1
        
    elif n == 3:
        p = 4
        
    elif n == 5:
        p = 7

    elif n == 9:
        p = 8
    else:
        print("Valor Inválido")
        break
    v = p*q
    t = t + v
print(f"O valor total foi de R${t:.2f}")
#sd

            
        