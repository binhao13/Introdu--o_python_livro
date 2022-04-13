n = int(input("Tabuada de: "))
i = int(input("Inicio da tabuada: "))
f = int(input("Fim da tabuada: "))
x = i
while x <= f:
    print(f"{n}x{x} = {n*x}")
    x += 1