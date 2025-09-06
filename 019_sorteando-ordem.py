import random
from time import sleep as sl

a1 = input('Digite o seu nome: ')
a2 = input('Digite o seu nome: ')
a3 = input('Digite o seu nome: ')
a4 = input('Digite o seu nome: ')
lista = [a1,a2,a3,a4]
random.shuffle(lista)

print('Sorteando a ordem de apresentação...')
sl(2)
print(f'A ordem de apresentação é:')
sl(1)
for nome in lista:
    print(nome)
    sl(2)
print('Boa sorte!')

