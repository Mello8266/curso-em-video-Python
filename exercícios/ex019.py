import random

nome1 = input('Insira o nome do primeiro aluno: ')
nome2 = input('Insira o nome do segundo aluno: ')
nome3 = input('Insira o nome do terceiro aluno: ')
nome4 = input('Insira o nome do quarto aluno: ')

lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)

print('O aluno escolhido foi: {}'.format(escolhido))