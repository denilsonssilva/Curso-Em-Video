import random
soma = 0
for i in range(6):
    n = random.randint(1, 100)
    if n % 2 == 0:
        print(n, end=' ')
        soma = soma + n
print(f'\nA soma de todos os números pares sorteados é {soma}.')

print('Acabou')