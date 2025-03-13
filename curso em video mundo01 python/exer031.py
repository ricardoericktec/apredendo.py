dis_viagem = float(input('qual a distancia da viagem em km? '))
if dis_viagem <= 200:
    preco = dis_viagem * 0.50
    print(f'o preço da viagem é de R${preco}')
else:
    preco = dis_viagem * 0.45
    print(f'o preço da viagem é de R${preco:}')