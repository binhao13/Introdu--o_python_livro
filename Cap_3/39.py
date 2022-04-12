d = int(input("Dias: "))
h = int(input("Horas: "))
m = int(input("Minutos: "))
s = int(input("Segundos: "))
t = d*24*60*60 + h*60*60 + m*60 + s
print(f"Isso representa {t} segundos")