admin = "eduardo"
senha = "12345"

limite = 0

def autenticar(a, p):
    if a.lower() == admin.lower():
            print("Usuário correto.")
    
            if p == senha:
                print("Senha correta.")

                return True

            else:
                print("Senha errada.")
                return False
    else:
        print("Usuário errado.")
        return False



while True:
    print("")
    a = str(input("Usuário: "))
    p = str(input("Senha: "))
    print("")

    answer = autenticar(a, p)

    if answer:
        break;
    else:
        limite +=1
        if limite==3:
            print("Acesso Bloqueado")
            exit()


print("Acesso autorizado")