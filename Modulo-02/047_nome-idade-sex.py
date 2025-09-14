nome = list()
idade = list()  
sexo = list()

for i in range(4):
    nome.append(input(f'Digite o nome da {i+1}ª pessoa: '))
    idade.append(int(input(f'Digite a idade da {i+1}ª pessoa: ')))
    sexo.append(input(f'Digite o sexo da {i+1}ª pessoa [M/F]: ').strip().upper()[0])
    print('---' * 10)

c = 0
for ano in idade:
    if ano < 20:
        for sexo in sexo:
            if sexo == 'F':
                c += 1
h = ''
i = 0
maior = max(idade)
for id in idade:
    if id == maior and sexo[i] == 'M':
        h = nome[h]
    i += 1
    

print(f'Ao todo, você cadastrou {len(nome)} pessoas.')
print(f'A média de idade é de {sum(idade)/len(idade):.1f} anos.')
print(f'O homem mais velho tem {max(idade)} anos e se chama {nome[h]}.')
print(f'A quantidade de mulheres menor de idade é {c}. ')




