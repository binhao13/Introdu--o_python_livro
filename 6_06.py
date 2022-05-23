último = 10
último2 = 10
fila = list(range(1,último + 1))
fila2 = list(range(1,último2 + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila 1")
    print(f"\nExistem {len(fila2)} clientes na fila 2")
    print("-------------------------------------------")
    print(f"Fila 1 atual: {fila}")
    print(f"Fila 2 atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila 1 e G para adicionar ao fim da fila 1,")
    print("ou A para realizar o atendimento da fila 1 e B para o atendimento da fila 2. S para sair.")
    operação = input("Operação (F,G,A,B ou S): ")
    x = 0
    sair = False
    while x < len(operação):
        if operação[x] == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido (FILA 1)")
            else:
                print("Fila 1 vazia! Ninuém para atender")
        elif operação[x] == "B":
            if len(fila2) > 0:
                atendido = fila2.pop(0)
                print(f"Cliente {atendido} atendido (FILA 2)")
            else:
                print("Fila 2 vazia! Ninuém para atender")
        elif operação[x] == "F":
            último += 1 #incrementa o ticket do novo cliente
            fila.append(último)
        elif operação[x] == "G":
            último2 += 1 #incrementa o ticket do novo cliente
            fila2.append(último2)
        elif operação[x] == "S":
            sair = True
            break
        else:
            print("Operação inválida! Digite apenas F,G,A,B ou S!")
        x += 1
    if sair:
            break        