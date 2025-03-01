import math
angulo = int(input('digite um angulo'))
angulo_r = math.radians(angulo)
seno = math.sin(angulo_r)
coseno = math.cos(angulo_r)
tangente = math.tan(angulo_r)
print(
    f' o seno é : {seno:.2f}\n o coseno é : {coseno:.2f}\n a tangente é : {tangente:.2f}')
