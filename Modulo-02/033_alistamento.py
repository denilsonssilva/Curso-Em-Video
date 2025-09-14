import datetime

anoa = datetime.date.today().year

ano = int(input('Digite seu ano de nascimento: '))
while ano >= anoa:
    ano = int(input('Ano invalido!\nDigite o seu ano de nascimento corretamente: '))

idade = anoa - ano

if idade == 18:
    print(f'Você tem {idade} anos, já esta na hora do alistamento.')
elif idade < 18:
    res = 18 - idade
    print(f'Prepare-se, faltam {res} anos para seu alistamento.')
else:
    print(f'Você tem {idade} anos, já passou o prazo de alistamento.')