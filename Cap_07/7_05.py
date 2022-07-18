s1 = input("Digite uma string: ")
s2 = input("Digite outra string: ")
s3 = ""
for a in s1:
    if a not in s2:
        s3 += a
if s3 == "":
    print("Não a caracteres")
else:
    print(s3)