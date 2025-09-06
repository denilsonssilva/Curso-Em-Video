import random
from time import sleep as sl

a1 = input('Digite seu nome: ')
a2 = input('Digite seu nome: ')
a3 = input('Digite seu nome: ')
a4 = input('Digite seu nome: ')
lista = [a1,a2,a3,a4]
sorteio = random.choice(lista)
print('Sorteando...')
sl(2)
print(f'O aluno sorteado é {sorteio}')