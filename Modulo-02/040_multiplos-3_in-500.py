for i in range(1, 501):
    if i % 3 == 0:
        if i % 2 != 0:
           print(i, end=' ')
    soma = sum(range(1, 501, 3))
print(f'\nA soma de todos os números ímpares múltiplos de 3 entre 1 e 500 é {soma}.')
print('Acabou')
