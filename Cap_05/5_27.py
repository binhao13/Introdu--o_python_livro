s = input("Digite o número a verificar: ")
i = 0
k = len(s) - 1
while k > i and s[i] == s[k]:
    i += 1
    k -= 1
if s[i] == s[k]:
    print("É palindromo")
else:
    print("Não é palindromo")
