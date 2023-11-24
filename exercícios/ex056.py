print('Insira o nome, idade e sexo de 5 pessoas.')

idadetotal = 0
velho = 0
mulher = 0
for c in range(0,5):
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo f ou m: ')).strip().lower()
    print('')

    idadetotal += idade
    
    if idade > velho:
        velho = idade
        nomevelho = nome
    
    if sexo == 'f' and idade < 21:
        mulher += 1

print('-' * 20)
media = idadetotal / 5
print(f'''Analisando os dados das 5 pessoas inseridas:
A média de idade do grupo é: {media}
A pesooa mais velha é o(a): {nomevelho}
Há {mulher} de mulheres menores de 21 anos''')