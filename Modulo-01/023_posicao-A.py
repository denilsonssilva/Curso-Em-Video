nome = input('Digite seu nome: ').upper().strip()

p = nome.count('A')

l = 'A'
pri = 0
ult = len(nome)
tot = ult - 1

while nome[tot] != 'A':
    tot -= 1

while nome[pri] != 'A':
    pri += 1

print(f'A letra A aparece {p} vezes.')
print(f'Primeira posição da letra A é: {pri}')
print(f'A ultima posição da letra A é: {tot}')

