import pygame

# Inicializa todos os módulos do Pygame
pygame.init()

# Carrega o arquivo de música
pygame.mixer.music.load("curso em video mundo01 python/ex0.mp3.mp3")

# Toca a música
pygame.mixer.music.play()

# Mantém o programa em execução enquanto a música toca
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)