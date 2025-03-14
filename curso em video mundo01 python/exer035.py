lado_1 = float(input('digite o primeiro lado do triangulo: '))
lado_2 = float(input('digite o segundo lado do triangulo: '))
lado_3 = float(input('digite o terceiro lado do triangulo: '))
if lado_1 < lado_2 + lado_3 and lado_2 < lado_1 + lado_3 and lado_3 < lado_1 + lado_2:
    print('os lados formam um triangulo')
else:
    print('os lados não formam um triangulo')
    