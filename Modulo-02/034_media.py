n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

med = (n1 + n2) / 2

if med < 5.0:
    print(f'\033[1;31mREPROVADO\033[m, sua média foi de {med}')
elif med >= 5.0 and med < 7.0:
    print(f'\033[1;33mRECUPERAÇÃO\033[m, sua média foi de {med}')
else:
    print(f'\033[1;32mAPROVADO\033[m, sua média foi de {med}')