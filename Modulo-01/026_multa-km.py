import random

vc = int(input('Qual a velocidade do carro?'))

km = 80

if vc > km:
    m = vc - km
    m = m * 7
    print(f'Você ultrapassou o limite de 80km/h. \nPague uma multa de \033[31mR${m:.2f} reais.\033[m')
else:
    print(f'Você esta dentro do limite {vc}km/h')

print('Tenha um Bom dia!')

