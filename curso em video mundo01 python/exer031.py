dis_viagem = float(input('qual a distancia da viagem em km? '))
if dis_viagem <= 200:
    print(f'o preço da viagem é de R${dis_viagem * 0.50}')
else:
    print(f'o preço da viagem é de R${dis_viagem * 0.45:}')