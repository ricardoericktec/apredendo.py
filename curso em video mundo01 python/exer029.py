vel = int(input('qual a velocidade do carro eem km/h? '))
if vel > 80:
    print(f'você foi multado em R${(vel - 80) * 7:.2f}')
else:
    print('siga seu caminho')