for i in range(5):
    peso = float(input(f'Digite o peso da {i+1}ª pessoa (kg): '))
    if i == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi de {maior} kg')
print(f'O menor peso lido foi de {menor} kg')

# Desafio 46 - Maior e menor peso