
idade = int(input("Idade: "))

if idade>=0 and idade<=12:
    print("Criança")

elif idade<=17:
    print("Adolescente")

elif idade<=59:
    print("Adulto")

elif idade>=60:
    print("Idoso")

else:
    print("Não pode valor negativo")
