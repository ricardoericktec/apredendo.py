# salario = [1518]
# def acresimo_salario(salario):
#     return salario + (salario * 0.15)
# reajuste = list(map(acresimo_salario, salario))
# print(reajuste)

salario = float(input('digite seu salario:'))
reajuste = salario + (salario * 0.15)

print(f'Seu salario reajustado é {reajuste}')
