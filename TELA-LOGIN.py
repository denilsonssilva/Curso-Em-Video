login = ['DENILSON','JORGE','MATHEUS']
senha = ['123','569','321']

#qtd e itens na lista
com = len(login)

tot = 0

logon = input('Você possui login? [S/N]').upper().strip()

while logon == 'S':

    loginU = input('Digite o seu login: ').upper().strip()#usuario
    senhaU = input('Digite sua senha: ').strip()#senha usuario

    for c in range (0, com):
        if login[c] == loginU and senha[c] == senhaU:
            print(f'Bem vindo ao Sistema {loginU}!')
            logon = login[c]
            tot += 1
    else:        
        print('Você digitou a senha/usuario errado, tente novamente!')
        logon = input('Deseja continuar? [S/N]').upper().strip()
    

if tot > 0:
    print(f'Obrigado, tenha um ótimo dia {logon}')
else:
    print('Você ainda não possui login! Deseja criar? [S/N]')
    



