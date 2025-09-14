n1 = int(input('Digite um número para verificar se é primo: '))

if n1 % 2 == 0 and n1 != 2:
    print(f'O número {n1} não é primo, pois é divisível por 2.')
else:
    print(f'O número {n1} é primo.')