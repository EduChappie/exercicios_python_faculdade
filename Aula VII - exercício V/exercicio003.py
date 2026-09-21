

def contar_palavras(frase):
    frase = frase.lower()

    palavras = frase.split()

    contador = {}

    for palavra in palavras:
        if palavra in contador:
            contador[palavra] += 1
        else:
            contador[palavra] = 1

    return contador

print("")
print("Entrada")
frase = input(": ")
print("")

resultado = contar_palavras(frase)

print(resultado)