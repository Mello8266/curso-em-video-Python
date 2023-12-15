tu = ()
print(type(tu))
for i in range(1, 5):
    tu += tuple(input('Digite um valor: '))
print(f'Você digitou os valores: {tu}')
print(f'O valor 9 foi digitado: {tu.count(9)} vezes')
print(f'O valor 3 está na {tu.index(3)} posição' if 3 in tu else 'O valor 3 não foi digitado.')