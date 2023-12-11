sexo = str(input('Insira seu sexo: ')).upper()
while sexo not in('F, M'):
    print('ERRO!\nInsira M ou F!')
    sexo = str(input('Insira seu sexo: ')).upper()
    print('')
print(f'Dado salva\nSeu gênero é {sexo}')