q = float(input("Digite a quantidade de cigarros fumados por dia: "))
a = float(input("Digite a quantidade de anos fumando: "))
q_c = q*a*365
p_min = 10*(q_c)
dias = p_min/24*60
print(f"A quantidade de dias perdidos é {dias} ")
