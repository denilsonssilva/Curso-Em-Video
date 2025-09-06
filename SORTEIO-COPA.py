import random
from time import sleep as sl

pote1 = ['PALMEIRAS','SAO PAULO','GREMIO','INTER','SANTOS','PSG','JUVENTUS','BARCELONA']
pote2 = ['CRUZEIRO','FLAMENGO','CORINTHIAS','VASCO','LIVERPOOL','MILAN','NEWCASTLE','BORUSSIA DORTMOND']
random.shuffle(pote1)
random.shuffle(pote2)
i = len(pote2)

print('Os confrontos das OITAVAS DE FINAL  são...')
print('='*30)
sl(2)
for time in pote1:
    print(f'\033[32m{time}\033[m X \033[31m{pote2[i-1]}\033[m')
    sl(2)
    i -= 1

print('='*30)




