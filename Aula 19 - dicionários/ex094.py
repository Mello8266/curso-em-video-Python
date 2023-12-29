temp = dict()
dado = list()
cont = total = 0

#? Acrescentando os dados no dicionário 
while True:
    temp['nome'] = str(input('Nome: ')).strip().capitalize()
    temp['sexo'] = str(input('Sexo: ')).strip().upper()[0]
    while temp['sexo'] not in ('F', 'M'):
        print('ERRO! Digite apenas M ou F.')
        temp['sexo'] = str(input('Sexo: ')).strip().upper()[0]
    temp['idade'] = int(input('Idade: '))
    dado.append(temp.copy()) # Adicionando o dicionário na lista
    conf = str(input('\nDeseja continuar? ')).strip().upper()[0]
    if conf == 'N':
        break

#? Analisando os dados
print('-=' * 20)
print(f'O grupo tem {len(dado)} pessoas')
for i in dado:
    total += i['idade'] 
media = total / len(dado)
print(f'A média de idade do grupo é {media:.2f}')

#? Exibindo a lista de mulheres
print('As mulheres cadastradas foram: ', end='')
for i in dado:
    if i['sexo'] == 'F':
        print(f'{i["nome"]} ', end='')
print()

#? Lista de pessoas acima da idade média
print('Lista de pessoas que estão acima da média:')
for i in dado:
    if i['idade'] >= media:
        print('    ', end='')
        for k, v in i.items():
            print(f'{k} = {v}; ', end='')
        print()
print('ENCERRADO')