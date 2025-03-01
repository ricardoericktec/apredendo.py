# manipulando cadeia de textos
frase = '   curso em video python'
# fatiamento

print(frase[9:14:2])  # imprime o caractere na posição 9

# análise

print(len(frase))  # comprimento da frase

print(frase.count('o',0,13))  # conta quantas vezes a letra 'o' aparece na frase

print(frase.find('deo'))  # encontra a posição onde começa a palavra 'deo' na frase

print(frase.find('Android'))  # retorna -1 se a palavra não for encontrada na frase

print('curso' in frase)  # verifica se a palavra 'curso' está na frase


# transformação 
print(frase.replace('python', 'android'))  # substitui a palavra 'python' por 'android' na frase

print(frase.upper())  # converte todos os caracteres da frase para maiúsculas

print(frase.lower())  # converte todos os caracteres da frase para minúsculas

print(frase.capitalize())  # converte apenas o primeiro caractere da frase para maiúscula e o resto para minúscula

print(frase.title())  # converte o primeiro caractere de cada palavra da frase para maiúscula e o resto para minúscula

print(frase.strip())  # remove espaços em branco do início e do fim da frase

print(frase.rstrip())  # remove espaços em branco do fim da frase

print(frase.lstrip())  # remove espaços em branco do início da frase


# divisão 

print(frase.split())  # divide a frase em uma lista de palavras, usando espaços em branco como separador


print(''.join(frase))  # junta os caracteres da frase em uma única string, usando '-' como separador