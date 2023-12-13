# Análise de dados
h = m = maior = cont = 0
while True:
    print('')
    print('=-=' * 15)
    print(f'{"CADASTRAMENTO":^45}')
    print('=-=' * 15)

    #nome = str(input('Insira o nome: '))
    idade = int(input('Insira a idade: '))
    sexo = str(input('Insira o sexo: [M/F] ')).strip().lower()[0]
    while sexo not in ('mf'):
        sexo = str(input('Insira o sexo: [M/F] ')).strip().lower()[0]

    if idade >= 18:
        maior += 1

    if sexo == 'm':
        h += 1

    if idade <= 20 and sexo == 'f':
        m += 1

    cont += 1

    print('=-=' * 15)
    conf = str(input('Deseja continuar adicionando dados? [S/N] ')).strip().lower()[0]
    while conf not in('s', 'n'):
        conf = str(input('Deseja continuar adicionando dados? [S/N] ')).strip().lower()[0]
    print('-' * 45)
    if conf == 'n':
        break

print(f'''
Você cadastrou {cont} pessoas
A quantidade de pessoas com idade maior que 18 é: {maior}
O total de homens cadastrados é: {h}
O total de mulheres com menos de 20 anos cadastradas é: {m}
''')