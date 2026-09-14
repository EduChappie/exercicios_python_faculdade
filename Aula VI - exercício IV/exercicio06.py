precos = [25.50, 40.00, 15.75, 80.00, 120.50]
soma = sum(precos)
superior = list(filter( lambda i: i>50, precos ))


for i in precos:
    print(i)

print("Soma preços: ", soma)
print("Média: ", soma/(len(precos)) )

print("\n")
print(*superior, sep="\n")
print(f"{len(superior)} valores acima de R$ 50")
