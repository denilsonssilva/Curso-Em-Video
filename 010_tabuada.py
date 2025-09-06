import time
n1 = int(input('Digite um numero e veja sua tabuada: '))

for i in range(1, 11):
    r = n1 * i
    time.sleep(0.5)
    print(f'{n1} * {i} = {r}')
