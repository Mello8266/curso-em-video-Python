nome = str(input('Insira seu nome completo: ')).strip()
nome = nome.split()
print('Primeiro nome é: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[len(nome) - 1]))