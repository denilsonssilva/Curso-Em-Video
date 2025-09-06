import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = math.hypot(co,ca)

print(f'O valor da hipotenusa é {h:.2f}')

