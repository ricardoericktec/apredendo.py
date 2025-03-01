# ponto 1 
frase = input("Digite uma frase: ").replace(" ", "")
letra_especifica = 'a'

frase_minuscula = frase.lower()

ocorrencias = frase_minuscula.count(letra_especifica)

print(f"A letra '{letra_especifica}' aparece {ocorrencias} vezes na frase.")


# ponto 2 
indice = frase.find(letra_especifica.upper())

print(f"A primeira ocorrência da letra '{letra_especifica}' está no índice {indice + 1}.")


# ponto 3 
indice = frase.rfind(letra_especifica)

print(f"A ultima ocorrência da letra '{letra_especifica}' está no índice {indice + 1}.")
