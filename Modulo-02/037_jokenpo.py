import random
from time import sleep as sl

p = input('Gostaria de jogar um jogo? [S/N]').upper().strip()
hum = 0
maq = 0

if p == 'S':
    print('-='*25)
    print('VAMOS JOGAR JOKENPÔ'.center(50))
    print('-='*25)
    sl(1)
    print('\033[31mPEDRA\033[m')
    sl(1)
    print('\033[32mPAPEL\033[m')
    sl(1)
    print('\033[33mTESOURA\033[m')
    sl(0.5)
    jog = input('Faça sua jogada: ').upper().strip()
    
    lista = ['PEDRA','PAPEL','TESOURA']
    pc = random.choice(lista)
    sl(0.5)
    print('\033[1mJO\033[m')
    sl(1)
    print('\033[1mKEN\033[m')
    sl(1)
    print('\033[1mPÔ\033[m')
    
    while p == 'S':
        if jog == 'PEDRA' and pc == 'TESOURA':
            print(f'\033[1;32mVocê venceu! {jog} derrota {pc}.\033[m')
            p = input('Gostaria de jogar mais uma vez? [S/N]').upper().strip()
            jog = input('Faça sua jogada: ').upper().strip()
            hum += 1
            pc = random.choice(lista)

        elif jog == 'TESOURA' and pc == 'PAPEL':
            print(f'\033[1;32mVocê venceu! {jog} derrota {pc}.\033[m')
            p = input('Gostaria de jogar mais uma vez? [S/N]').upper().strip()
            jog = input('Faça sua jogada: ').upper().strip()
            hum += 1
            pc = random.choice(lista)

        elif jog == 'PAPEL' and pc == 'PEDRA':
            print(f'\033[1;32mVocê venceu! {jog} derrota {pc}.\033[m')
            p = input('Gostaria de jogar mais uma vez? [S/N]').upper().strip()
            jog = input('Faça sua jogada: ').upper().strip()
            hum += 1
            pc = random.choice(lista)

        elif jog == pc:
            print(f'\033[1;33mTemos um empate! {jog} x {pc}.\033[m')
            p = input('Gostaria de jogar mais uma vez? [S/N]').upper().strip()
            jog = input('Faça sua jogada: ').upper().strip()
            pc = random.choice(lista)

        else:
            print(f'\033[1;31mVocê Perdeu! {pc} derrota {jog}.\033[m')
            p = input('Gostaria de jogar mais uma vez? [S/N]').upper().strip()
            jog = input('Faça sua jogada: ').upper().strip()
            maq +=1
            pc = random.choice(lista)

if hum != 0 or maq != 0: 
    print('RESULTADO...')
    sl(2)
    if hum > maq:
        print(f'\033[1;32mParabéns você derrotou a Máquina\033[m')
        print(f'\033[1;32mJogador:\033[m {hum} \n\033[1;31mMaquina:\033[m {maq}')
    elif maq > hum:
        print(f'\033[1;31mA Máquina venceu!\033[m')
        print(f'\033[1;31mMaquina:\033[m {maq} \n\033[1;32mJogador:\033[m {jog}')
    else:
        print(f'\033[1;33mTivemos um empate\033[m')
        print(f'\033[1;33mJogador:\033[m {hum} \n\033[1;31mMaquina:\033[m {maq}')

print('OBRIGADO POR JOGAR!')




