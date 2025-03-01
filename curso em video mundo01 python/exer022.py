# ponto 1
nome = input("Digite seu nome: ")
print(f'seu nome em maiusculo é {nome.upper()}')
print(f'seu nome em minusculo é {nome.lower()}')

# ponto 2
print(f'seu nome ao todo tem {len(nome.replace(" ", ""))}')
# ponto 3

# print(f'seu primeiro nome tem {len(nome.split()[0])} letras')
separar = nome.split()
print(f'seu primeiro nome é {separar[0]} e ele tem {len(separar[0])} letras')
