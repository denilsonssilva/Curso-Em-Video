v = int(input('Qual a distancia sua viagem em Km: '))

if v <= 200:
    p = v * 0.50
    print(f'Para sua viagem de {v}Km, \nVocê pagara R${p:.2f} reais.')
else:
    p = v * 0.45
    print(f'Para sua viagem de {v}Km, \nVocê pagara R${p:.2f} reais.')