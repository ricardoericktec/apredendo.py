# c_adjasente = float(input('digite o cateto adjacente'))
# c_oposto = float(input('digite o cateto oposto'))
# hipotnusa = float(c_adjasente ** 2) + (c_oposto ** 2)
# print(f'a hipotnusa é {hipotnusa ** (1/2):.2f}')
import math
c_adjasente = float(input('digite o cateto adjacente'))
c_oposto = float(input('digite o cateto oposto'))
hipotnusa = math.hypot(c_adjasente, c_oposto)
print(hipotnusa)
