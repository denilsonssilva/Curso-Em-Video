peso = float(input('Quantos kg você pesa? '))
altura = float(input('Qual a sua altura? '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f}, você esta abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é de {imc:.2f}, você esta no peso ideal.')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é de {imc:.2f}, você esta sobrepeso.')
elif imc >= 30 and imc < 40:
    print(f'Seu IMC é de {imc:.2f}, você esta obeso.')
else:
    print(f'Seu IMC é de {imc:.2f}, você esta com obesidade mórbida.')