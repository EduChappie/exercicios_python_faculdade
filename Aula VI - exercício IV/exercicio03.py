
l = list(range(1, 51))

soma = sum(l)
soma_pares = sum([ i for i in l if i%2==0 ])
soma_impares = sum([ i for i in l if i%2!=0 ])

print(l)
print(soma)
print(soma_pares)
print(soma_impares)

