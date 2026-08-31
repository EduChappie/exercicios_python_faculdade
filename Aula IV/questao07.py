
nota = float(input("Nota:"))

if nota>=0 and nota<=4.9:
    print("Reprovado")
    
elif nota>=5 and nota<=6.9:
    print("Recuperação")

elif nota>=7 and nota<=10:
    print("Aprovado")

else:
    print("nota não condiz com o pedido, está maior que 10 ou menor que 0")
