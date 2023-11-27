print('Insira o nome, idade e sexo de 5 pessoas.')

idadetotal = 0
velho = 0
mulher = 0
for c in range(1, 5):
    nome = str(input(f'{c}º nome: ')).strip().capitalize()
    idade = int(input(f'{c}º idade: '))
    sexo = str(input(f'{c}º sexo f ou m: ')).strip()
    print('')

    idadetotal += idade
    
    if c == 1 and sexo in 'Mm':
        velho = idade
        nomevelho = nome

    if idade > velho and sexo in 'Mm':
        velho = idade
        nomevelho = nome
    
    if sexo == 'f' and idade < 20:
        mulher += 1

print('-' * 20)
media = idadetotal / 4
print(f'''Analisando os dados das 5 pessoas inseridas:
A média de idade do grupo é: {media}
O homem mais velho é o: {nomevelho} que tem {velho} anos
Há {mulher} mulheres menores de 21 anos''')