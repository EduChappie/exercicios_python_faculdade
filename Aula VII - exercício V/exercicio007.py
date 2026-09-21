def analisar_texto(texto):
    total_caracteres = len(texto)
    letras = 0
    numeros = 0
    espacos = 0
 
    i = 0
    while i < len(texto):
        caractere = texto[i]
        if caractere.isalpha():
            letras += 1
        elif caractere.isdigit():
            numeros += 1
        elif caractere == " ":
            espacos += 1
        i += 1
 
    palavras = len(texto.split())
 
    return total_caracteres, letras, numeros, espacos, palavras
 
 
frase = input("Digite uma frase: ")
total_caracteres, letras, numeros, espacos, palavras = analisar_texto(frase)

print("")
print(f"Quantidade total de caracteres: {total_caracteres}")
print(f"qtd de letras: {letras}")
print(f"qtd de números: {numeros}")
print(f"qtd de espaços: {espacos}")
print(f"qtd de palavras: {palavras}")