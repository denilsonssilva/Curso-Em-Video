valorFinan = float(input('Qual o valor do imovel? R$'))
sal = float(input('Qual o seu salario? R$'))
prazo = int(input('Em quantos anos você gostaria de pagar o financiamento? '))
prazo = prazo * 12

parcela = sal * 0.30
mensal = valorFinan / prazo

if parcela < mensal:
    print('\033[1;31mEmprestimo Negado\033[m')
    print(f'\033[1;31mAs parcelas de R${mensal:.2f} excederam os 30% do seu salario.\033[m')
else:
    print(f'\033[1;32mEmprestimo de R${valorFinan:.2f} aprovado, \nPara ser pago em {prazo} meses.\033[m')
    print(f'\033[1;32mCom parcelas de R${mensal:.2f} reais.\033[m')
