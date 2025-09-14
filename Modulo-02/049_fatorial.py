import math

n1 = int(input('Digite um numero: '))

mult = n1
for i in range(n1, 0, -1):
    print(f'{i}', end='')
    print(' x ' if i > 1 else ' = ', end='')
    

print(math.factorial(n1))