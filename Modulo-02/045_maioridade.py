import datetime
anoatual = datetime.date.today().year

c = 0

for i in range(7):
    anonascimento = int(input(f'Digite a idade da {i+1}ª pessoa: '))
    idade = anoatual - anonascimento
    if idade >= 21:
        print('Maior de idade')
        c += 1
    else:
        print('Menor de idade')

print(f'Ao todo tivemos {c} pessoas maiores de idade e {7-c} pessoas menores de idade.')