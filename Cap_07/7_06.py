s1 = input("Digite uma string: ")
s2 = input("Digite outra string: ")
s3 = input("Digite outra string: ")
if len(s2) == len(s3):
    s4 = ""
    for letra in s1:
        posicao = s2.find(letra)
        if posicao > -1:
            s4 += s3[posicao]
        else:
            s4 += letra
    if s4 == "":
        print("Todos os caracteres foram removidos")
    else:
        print(s4)
else:
    print("""ERROR
A segunda dtring e a terceira devem ter o mesmo tamanho""")