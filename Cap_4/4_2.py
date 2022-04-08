v = float(input("Digite a velocidade do carro: "))
if v > 80:
    print("Você foi multado")
    m = v - 80
    pm = 5*m
    print(f"O valor da sua multa é de R${pm:.2f} ")
else:
    print("De boa")