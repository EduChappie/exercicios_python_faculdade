
nomes = ["Eduardo", "Maria", "João", "Pedro", "Laura", "Marcelo", "Arrascaeta", "Bruno", "Carrascal", "Neuer"]
nomes6 = list(filter(
    lambda i:
    len(i)>6,
    nomes
))

print("Nomes:")
print(*nomes, sep="\n")

print(f"\nNomes com mais de 6: {len(nomes6)}")
print(*nomes6, sep="\n")
