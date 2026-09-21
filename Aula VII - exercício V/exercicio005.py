def validar_senha(senha):
    maisc = False
    minus = False
    num = False
 
    for caractere in senha:
        if caractere.isupper():
            maisc = True
        elif caractere.islower():
            minus = True
        elif caractere.isdigit():
            num = True
 
    return len(senha) >= 8 and maisc and minus and num


 
senha_valida = False
while not senha_valida:
    senha = input("Digite uma senha: ")
 
    if validar_senha(senha):
        senha_valida = True
        print("Senha válida!")
    else:
        print("Senha inválida. Deve ter no mínimo 8 caracteres, uma letra maiúscula, uma minúscula e um número.")
 