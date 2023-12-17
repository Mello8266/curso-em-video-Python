a = int(input('Digite um valor: '))
b = int(input('Digite mais um valor: '))
c = int(input('Digite outro valor: '))
d = int(input('Digite o último valor: '))

tupla = ('', a, b, c, d )
 
print(f'Você digitou os valores: {tupla[1:]}')
print(f'O valor 9 foi digitado: {tupla.count(9)} vezes')
print(f'O valor 3 está na {tupla.index(3)} posição' if 3 in tupla else 'O valor 3 não foi digitado.')