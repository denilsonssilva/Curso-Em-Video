frase = input('Digite uma palavra: ').strip().upper()
inverso = frase[::-1]
if frase == inverso:
    print(f'A palavra {frase} é um palíndromo.')        
else:
    print(f'A palavra {frase} não é um palíndromo.')

print('Acabou')
