sal = float(input('Digite o seu salario atual: R$'))

z = 1250.00

if sal > z:
    aum = sal * 0.10
    print(f'Seu salario de R${sal:.2f}, ganhou um aumento de R${aum:.2f}')
    print(f'Você passará a receber R${sal+aum}')
else:
    aum = sal * 0.15
    print(f'Seu salario de R${sal:.2f}, ganhou um aumento de R${aum:.2f}')
    print(f'Você passará a receber R${sal+aum}')