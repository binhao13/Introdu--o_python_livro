while True:
    print("""

Menu
----
1 - Adição
2 - Subtração
3 - Divisão
4 - Multiplicação
5 - Sair

""")
    opção = int(input("Escolha uma opção:"))
    if opção == 5:
        break
    elif opção >= 1 and opção < 5:
        n = int(input("Tabuada de:"))
        x = 1
        while x <= 10:
            match opção:
                case 1:
                    print(f"{n} + {x} = {n + x}")
                case 2:
                    print(f"{n} - {x} = {n - x}")
                case 3:
                    print(f"{n} / {x} = {n / x:5.4f}")
                case 4:
                    print(f"{n} x {x} = {n * x}")
            x = x + 1
    else:
        print("Opção inválida!")