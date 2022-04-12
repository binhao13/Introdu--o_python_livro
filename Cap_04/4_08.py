y = float(input("Digite um número: "))
z = float(input("Digite um número: "))
x = input("Digite que operação deseja realizar (+ || - || / || * ||): ")
if x == "+":
    print(f"{y} + {z} = {y+z}")
elif x == "-":
    print(f"{y} - {z} = {y-z}")
elif x == "/":
    print(f"{y}/{z} = {y/z}")
elif x == "*":
    print(f"{y} * {z} = {y*z}")
else:
    print("inválido")
    




    