divida = float(input("Digite o valor da sua divida: "))
jm = float(input("Digite o valor dos juros mensais: "))
vpm = float(input("Digite o valor pago mensalmente: "))
if (divida*(jm/100) >= vpm):
    print("Sua divida não será paga nunca")
else:
    m = 1
    jp = 0
    saldo = divida
    tp = 0
    while saldo > vpm:
        print(f"Mês:{m}")
        jmp = jm/100
        va = (saldo*(1 + jmp))
        tp = tp + vpm
        print(f"Total pago: R${tp:.2f}")        
        saldo = va - vpm
        print(f"Valor da divida: R${saldo:.2f}")
        m += 1
        jp = jp + va*jmp
        print(f"Valor dos juros acumulados: R${jp:.2f}")
    if saldo > 0:
        tp = tp + saldo
    print("-----------------------")
    print(f"Número de meses:{m}\nTotal pago: R${tp:.2f}\nJuros pagos: R${jp:.2f}")


    
