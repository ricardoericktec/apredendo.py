import random
import time
num_usuario = int(input('Digite um número de 0 a 5: '))
num_misterioso = random.randint(0, 5)  # Corrigido para usar randint em vez de choice
print('Processando...')
time.sleep(4)
if num_usuario == num_misterioso:
    print('Parabéns, você acertou!')
else:
    print(f'voce errou o numero era {num_misterioso}')