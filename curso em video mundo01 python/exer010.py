# o codigo abaixo e para saber a quantidaded de tinta que presisa pra saber pinta uma parede
altura = int(input('Digite a altura da parede: '))
largura = int(input('Digite a largura da parede: '))
area = altura * largura
tinta = 2
litros = area / tinta
print(f'A parede tem {area}m² e precisa de {litros} litros de tinta para ser pintada')
