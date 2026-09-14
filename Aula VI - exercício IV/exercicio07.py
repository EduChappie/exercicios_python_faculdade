temperaturas = [28, 30, 27, 31, 29, 32, 26]
media = sum(temperaturas)/len(temperaturas)

for t in temperaturas:
    print(t)

print("Média: ", media)

print("Maior valor: ", max(temperaturas))
print("Menor valor: ", min(temperaturas))

acimaMedia = list(filter(
    lambda i:
    i>media,
    temperaturas
))
print(f"Existiram {len(acimaMedia)} dias acima da média")