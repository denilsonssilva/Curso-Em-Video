sexo = input('Digite o seu sexo: [M/F] -> ').upper().strip()

while sexo != 'F' and sexo != 'M':
    print('\033[31mDigite novamente!!!\033[m')
    sexo = input('Digite o seu sexo: [M/F] -> ').upper().strip()
if sexo == 'F':
    sexo = 'Feminino'
else:
    sexo = 'Masculino'

print(f'Parabéns, seu sexo é {sexo}')