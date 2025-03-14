salario = float(input('Qual é o salário do funcionário? R$: '))
if salario <= 1250:
    print(f'quem ganhava R${salario:.2f} passa a ganhar R${salario + (salario * 15 / 100):.2f} agora')
else:
    print(f'quem ganhava R${salario:.2f} passa a ganhar R${salario + (salario * 10 / 100):.2f} agora')