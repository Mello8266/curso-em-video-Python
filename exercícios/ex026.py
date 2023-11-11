frase = str(input('Insira uma frase: ')).lower().strip()
print('Total de letras a na frase: {}'.format(frase.count('a')))
print('Posição do primeiro a: {}'.format(frase.find('a') + 1))
print('A última letra está na posição: {}'.format(frase.rfind('a') + 1))
