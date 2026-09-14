
notas = [7.5, 8.0, 6.5, 9.0, 5.5, 8.5]
aprovados = list(filter(lambda i: i>=7.0, notas))

for i in range(len(notas)):
    print(notas[i])


print("Média: ",  (sum(notas) / (len(notas))) )
print("Aprovados: ", list(filter(lambda i: i>=7.0, notas)))
print("QTD: ", len(aprovados))
