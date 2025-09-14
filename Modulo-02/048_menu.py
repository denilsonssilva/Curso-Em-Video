from time import sleep as sl

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

def menu():
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos numeros')
    print('[5] sair')
    print('---- O que gostaria de fazer agora? ----')

menu()
escolha = int(input('Faça sua escolha: '))

while escolha != 5:
    menu()
    if escolha == 1:
        print(f'A soma entre {n1} e {n2} é {n1+n2}')
        print('='*30)
        sl(1)
        menu()
        escolha = int(input('Faça sua escolha: '))

    elif escolha == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1*n2}')
        print('='*30)
        sl(1)
        menu()
        escolha = int(input('Faça sua escolha: '))

    elif escolha == 3:
        print(f'O maior numero entre {n1} e {n2} é {max(n1,n2)}')
        print('='*30)
        sl(1)
        menu()
        escolha = int(input('Faça sua escolha: '))

    elif escolha == 4:
        print('---- Digite novos valores ----')
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
        print('='*30)
        sl(1)
        menu()
        escolha = int(input('Faça sua escolha: '))
    else:
        break

print('Finalizando..')
sl(1)
print('Obrigado pela interação.')