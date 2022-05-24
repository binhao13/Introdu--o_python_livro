t = [-10,-8,0,1,2,5,-2,-4]
minimo = t[0]
maximo = t[0]
s = 0
for e in t:
    if e <= minimo:
        minimo = e
    if e >= maximo:
        maximo = e
    s = s + e
m = s/len(t)
print(f"""A temperatura minima é {minimo}°C
A temperatura máxima é {maximo}°C
A temperatura média é {m}°C""")