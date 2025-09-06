nome = input('Digite o seu nome completo: ')
maius = nome.upper()
minus = nome.lower()
cont = nome.split()
pn = len(cont[0])
tot = 0

for i in range(len(nome)):
    if nome[i] != ' ':
        tot += 1

print(f'Total de letras: {tot} ')
print(f'TUDO EM MAIUSCULO: {maius}\ntudo em minusculo: {minus}')
print(f'Total de letras no primeiro nome: {pn}')

