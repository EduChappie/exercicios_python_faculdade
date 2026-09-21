clientes = []


def cadastrar_cliente():
    nome = input("Nome: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")

    cliente = {"nome": nome, "email": email, "telefone": telefone}
    clientes.append(cliente)
    print("Cliente cadastrado!")


def pesquisar_cliente():
    nome_busca = input("Digite o nome do cliente: ").lower()

    for cliente in clientes:
        if cliente["nome"].lower() == nome_busca:
            print(f"Nome: {cliente['nome']}")
            print(f"E-mail: {cliente['email']}")
            print(f"Telefone: {cliente['telefone']}")
            return

    print("Cliente não encontrado.")


def listar_clientes():
    print("")
    print("clientes: ")
    for cliente in clientes:
        print(f"{cliente['nome']} - {cliente['email']} - {cliente['telefone']}")


answer = 0
while answer != 4:
    print("")
    print("1 - Cadastrar cliente")
    print("2 - Pesquisar cliente")
    print("3 - Listar clientes")
    print("4 - Sair")

    answer = int(input("Escolha uma opção: "))

    if answer == 1:
        cadastrar_cliente()
    elif answer == 2:
        pesquisar_cliente()
    elif answer == 3:
        listar_clientes()
    elif answer == 4:
        print("fechando")
    else:
        print("opção inexistente")