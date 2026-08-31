n1 = float(input("numero 1: "))
n2 = float(input("numero 2: "))
s = 0
answer = input("Escolha entre essas operações(+, -, *, /): ")

while not answer in ["+", "-", "*", "/"]:
    print("Operação inexistente")
    answer = input("Escolha entre essas operações(+, -, *, /): ")

if answer=="+":
    s = n1+n2
elif answer=="-":
    s = n1-n2
elif answer=="*":
    s = n1*n2
elif answer=="/":
    s = n1/n2

print(s)
