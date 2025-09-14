vp = float(input('Valor do produto: R$'))
fp = input('Qual a forma de pagamento?' ).strip().lower()
if fp == 'cartao':
    par = int(input('Em quantas vezes gostaria de parcelar? '))


if fp == 'dinheiro' or fp == 'cheque':
    des = vp * 0.10
    print(f'O produto ganhou um desconto de R${des:.2f}')
    print(f'Novo valor do produto R${vp - des:.2f}')
elif fp == 'cartao' and par < 2:
    des = vp * 0.05
    print(f'O produto ganhou um desconto de R${des:.2f}')
    print(f'Novo valor do produto R${vp - des:.2f}')
elif fp == 'cartao' and par == 2:
    print(f'O produto não obteve desconto. Valor da compra R${vp:.2f}')
elif fp == 'cartao' and par > 2:
    jur = vp * 0.2
    print(f'O cliente pagará R${jur:.2f} de juros')
    print(f'Novo valor do produto R${vp + jur:.2f}')