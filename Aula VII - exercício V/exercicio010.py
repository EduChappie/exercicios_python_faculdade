estudantes = []


def cadastrar_estudante():
    nome = input("Nome do estudante: ")
    nota = float(input("Nota: "))

    estudante = {"nome": nome, "nota": nota}
    estudantes.append(estudante)
    print("Estudante cadastrado!")


def calcular_media():
    total = 0
    for estudante in estudantes:
        total += estudante["nota"]
    return total / len(estudantes)


def maior_nota():
    maior = estudantes[0]
    for estudante in estudantes:
        if estudante["nota"] > maior["nota"]:
            maior = estudante
    return maior


def listar_aprovados():
    print("")
    print("aprovados:")
    for estudante in estudantes:
        if estudante["nota"] >= 7.0:
            print(f"{estudante['nome']} - Nota: {estudante['nota']}")


answer = 0
while answer != 5:
    print("")
    print("1 - Cadastrar estudante")
    print("2 - Exibir média da turma")
    print("3 - Exibir estudante com maior nota")
    print("4 - Listar aprovados")
    print("5 - Sair")

    answer = int(input("Escolha uma opção: "))

    if answer == 1:
        cadastrar_estudante()
    elif answer == 2:
        print(f"Média da turma: {calcular_media():.2f}")
    elif answer == 3:
        estudante = maior_nota()
        print(f"Maior nota: {estudante['nome']} - {estudante['nota']}")
    elif answer == 4:
        listar_aprovados()
    elif answer == 5:
        print("fechando")
    else:
        print("opção não valeu!")