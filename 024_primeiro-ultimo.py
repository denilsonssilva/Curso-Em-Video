nome = input('Digite seu nome completo: ').upper()

nome = nome.split()
ultimo = len(nome)

print(f'Primeiro nome: {nome[0]}')
print(f'Ultimo nome: {nome[ultimo-1]}')
