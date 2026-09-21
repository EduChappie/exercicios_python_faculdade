carrinho = []
 
 
def calcular_total(carrinho):
    total = 0
    for produto in carrinho:
        total += produto["quantidade"] * produto["preco"]
    return total
 
 
continuar = "s"
while continuar == "s":
    print("")
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
 
    produto = {"nome": nome, "quantidade": quantidade, "preco": preco}
    carrinho.append(produto)
 
    continuar = input("Adicionar outro produto? (s/n): ")

print("")
print("carrinho: ")
for produto in carrinho:
    print(f"{produto['nome']} - Qtd: {produto['quantidade']} - R$ {produto['preco']:.2f}")
 
print(f"\nTotal da compra: R$ {calcular_total(carrinho):.2f}")
 