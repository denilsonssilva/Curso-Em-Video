cid = input('Dgite o nome da sua Cidade: ').strip().lower()
cid = cid.split()

if cid[0] == 'santo':
    print(f'O nome da sua cidade contém a palavra SANTO.')
else:
    print(f'O nome da sua cidade não tem SANTO.')