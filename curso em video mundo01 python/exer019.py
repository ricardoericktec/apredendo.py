import random
p1 = input('nome do primeiro aluno:')
p2 = input('nome do segundo aluno:')
p3 = input('nome do terceiro aluno:')
p4 = input('o nome do quarto aluno:')
lista = [p1, p2, p3, p4]
aluno_s = random.choice(lista)
print(f'o aluno escolhido foi {aluno_s}')

