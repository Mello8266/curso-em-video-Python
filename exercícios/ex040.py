nota1 = float(input('Insira a primeira nota do aluno: '))
nota2 = float(input('Insira a segunda nota do aluno: '))

media = (nota1 + nota2) / 2
print(f'A média do aluno é {media:.2f}')

if media >= 7:
    print('Aluno aprovado')

elif media < 5:
    print('Aluno reprovado')

else:
    print('Aluno em recuperação')