tarefas = []
 
 
def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada!")
 
 
def listar_tarefas():
    print("")
    print("tarefas: ")
    for indice, tarefa in enumerate(tarefas, start=1):
        print(f"{indice} - {tarefa}")
 
 
def remover_tarefa():
    listar_tarefas()
    indice = int(input("Digite o número da tarefa a remover: "))
    tarefas.pop(indice - 1)
    print("Tarefa removida!")
 
 
answer = 0
while answer != 4:
    print("")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")
 
    answer = int(input("Escolha uma opção: "))
 
    if answer == 1:
        adicionar_tarefa()
    elif answer == 2:
        listar_tarefas()
    elif answer == 3:
        remover_tarefa()
    elif answer == 4:
        print("fechando")
    else:
        print("num valeu")