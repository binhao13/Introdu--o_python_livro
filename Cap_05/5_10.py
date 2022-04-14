p = 0
q = 1
while q <= 3:
    r = input(f"Resposta da questão {q}: ")
    if q == 1 and (r == "b" or r == "B"):
        p += 1
    if q == 2 and (r == "a" or r == "A"):
        p += 1
    if q == 3 and (r == "d" or r == "D"):
        p += 1
    q += 1
print(f"O aluno fez {p} ponto(s)")