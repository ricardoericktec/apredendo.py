salario = float(input('Qual é o salário do funcionário? R$: '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print(f'quem ganhava R${salario:.2f} passa a ser R${novo:.2f} agora')
else:
    novo = salario + (salario * 10 / 100)
    print(f'quem ganhava R${salario:.2f} passa a ser R${novo:.2f} agora')