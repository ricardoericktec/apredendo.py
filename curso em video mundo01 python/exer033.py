num_1 = int(input('digite o primeiro numero: '))
num_2 = int(input('digite o segundo numero: '))
num_3 = int(input('digite o terceiro numero: '))
if num_1 > num_2 and num_1 > num_3:
    print(f'o maior numero é {num_1}')
elif num_2 > num_1 and num_2 > num_3:
    print(f'o maior numero é {num_2}')
else:
    print(f'o maior numero é {num_3}')  