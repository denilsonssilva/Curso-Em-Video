
lista = []

for i in range(4):
    n1 = int(input('Digite um numero: '))
    lista.append(n1)

i = 0
m = 0

for n in lista:
    if i == 0:
        i = n
        m = n
        
    elif n > m:
        i = n
    elif n < m:
        m = n

print(f'Menor = {m}')
print(f'Maior = {i}')