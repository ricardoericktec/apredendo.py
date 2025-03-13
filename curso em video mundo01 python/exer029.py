vel = int(input('qual a velocidade do carro eem km/h? '))
if vel > 80:
    print('você foi multado')
    multa = (vel - 80) * 7
    print(f'você foi multado em R${multa:.2f}')
else:
    print('você não foi multado')