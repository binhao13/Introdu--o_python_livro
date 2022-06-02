s1 = input("Digite a primeira string: ")
s2 = input("Digite a segunda string: ")
s3 = ""
q = 0
t = 0
for letra in s1:
    q = s2.find(letra)
    if q == -1:
        s3 += letra
for letra2 in s2:
    t = s1.find(letra2)
    if t == -1:
        s3 += letra2
s3 = set(s3)
s3 = "".join(s3)
print(s3)