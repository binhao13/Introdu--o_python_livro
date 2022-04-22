n = int(input("Digite um número: "))
x = 3
if n < 0:
    print("Não é primo")
    exit
elif n == 0 or n == 1:
    print("Não é primo")
    exit
elif n == 2:
        print("É primo")
elif n % 2 == 0:
    print("Não é primo")
else:
    while x < n:
        if n % x == 0:
            print("Não é primo")
            break
        x += 2
    if x == n:
        print("É primo")
        