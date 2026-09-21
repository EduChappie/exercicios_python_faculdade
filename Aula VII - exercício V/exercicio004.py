estudantes = {}


def calcular_media(notas):
    return sum(notas) / len(notas)


cadastrar = "s"

while cadastrar != "n":
    nome = input("Nome do estudante: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    estudantes[nome] = [nota1, nota2, nota3]

    cadastrar = input("Cadastrar outro estudante? (s/n): ")



print("")
for nome, notas in estudantes.items():
    media = calcular_media(notas)

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    print(f"Nome: {nome}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
    print("-" * 20)