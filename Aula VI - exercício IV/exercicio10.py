l = []


for i in range(10):
    r = int(input(f"Digite um número inteiro: [{i+1}]"))
    l.append(r)


media = sum(l)/len(l)

print(f"""
{l}
===== RELATÓRIO =====
Quantidade de números: {len(l)}
Soma: {sum(l)}
Média: {media}
Maior valor: {max(l)}
Menor valor: {min(l)}
Quantidade de pares: {len([ n for n in range(len(l)) if l[n]%2==0 ])}
Quantidade de ímpares: {len([ n for n in range(len(l)) if l[n]%2!=0 ])}
Acima da Média: {list(filter(
    lambda i:
    i>media,
    l
))}
=====================
""")