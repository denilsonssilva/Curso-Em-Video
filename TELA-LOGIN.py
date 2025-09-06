login = ['DENILSON','JORGE','MATHEUS']
senha = ['123','569','321']

tot = 0
#Pergunta se o usuario tem login
logon = input('Você possui login? [S/N]').upper().strip()

while logon == 'S':
    
    loginU = input('Digite o seu login: ').upper().strip()#usuario
    senhaU = input('Digite sua senha: ').strip()#senha usuario

    for nome in login: #percorre toda a lista 'login' e adiciona cada posição a variavel nome
        for sen in senha: #percorre toda a lista 'senha' e adiciona cada posição a variavel sen
            if nome == loginU and sen == senhaU:
                logon = nome
                tot += 1
    
    if tot > 0:
        print(f'Bem vindo ao Sistema {nome}!')
    else:
        print('Você digitou a senha/usuario errado, tente novamente!')
        logon = input('Deseja continuar? [S/N]').upper().strip()
    

if tot > 0:
    print(f'Obrigado, tenha um ótimo dia {logon}')
else:
    print('Você ainda não possui login! Deseja criar? [S/N]')
    



