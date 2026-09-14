vendas = [15, 22, 18, 30, 25, 20]
media = sum(vendas)/len(vendas)

for i in vendas:
    print(i)

print("Vendidos total: ", sum(vendas))
print(f"Média de vendas: {media:.2f}")
print("Dias acima da média: ", *[f"{n} -" for n in range(len(vendas)) if vendas[n]>media])