produtos = {}

def cadastrar_produtos(prod, nome, preco):

    if preco <= 0:
        return print("Valor inválido")
    
    else:
        prod[nome] = preco
        return print("Cadastrado com Sucesso")

    

while True:
    print("")
    n = str(input("Nome do produto: "))
    p = float(input("Preço do produto: "))
    print("")

    cadastrar_produtos(produtos, n, p)

    print("Deseja continuar cadastrando? (s/n)")
    answer = str(input("-> ")).lower()

    if answer=="n" or answer=="nao" or answer=="não": 
        break 
    else: 
        continue

for i in produtos:
    print(f"Produto: {i} - Preço: {produtos[i]}")