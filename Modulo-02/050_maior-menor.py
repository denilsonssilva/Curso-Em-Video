numeros = list()

numeros.append(int(input('Digite um numero inteiro: ')))
cont = input('Gostaria de continuar? [S/N]: ').upper().strip()

while cont == 'S':
    numeros.append(int(input('Digite um numero inteiro: ')))
    cont = input('Gostaria de continuar? [S/N]: ').upper().strip()

print(f'A média entre os valores digitados é {sum(numeros)/len(numeros):.2f}')
print(f'O maior valor é {max(numeros)}')
print(f'O menor valor é {min(numeros)}')
