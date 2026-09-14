lista = []


for i in range(10):
    r = 0
    r = int(input(f"Digite um número inteiro [{i+1}]:"))
    lista.append(r)

print("\n")
print(*lista, sep="\n")

p = [ i for i in lista if i>0 ]
n = [ i for i in lista if i<0 ]
z = [ i for i in lista if i==0 ]

print(f"Positivo {len(p)}: ", p)
print(f"Negativo {len(n)}: ", n)
print(f"Zeros {len(z)}: ", z)

