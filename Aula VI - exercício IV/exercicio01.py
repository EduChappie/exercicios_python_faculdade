
lista = list(range(1, 21))

lista_pares = [ n for n in lista if n%2==0 ]

print("Lista: ", lista)
print("Pares: ", lista_pares)
print("Qtd_pares: ", len(lista_pares))
