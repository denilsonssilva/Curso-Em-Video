import random

n1 = int(input('Tente adivinhar qual numero estou pensando de 0 a 5: '))

pc = random.randint(0, 5)

while n1 != '':
    if n1 == pc:
        print(f'\033[32mParabéns, o numero que eu estava pensando era o \033[32m{pc}.\033[m')
    else:
        print(f'\033[31mO numero que eu pensei foi o \033[31m{pc}.\033[m')
        n1 = int(input('Tente novamente, qual numero estou pensando de 0 a 5? '))
        pc = random.randint(0, 5)





