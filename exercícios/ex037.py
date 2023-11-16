print('Conversão númerica')
num = int(input('Isira um número inteiro: '))
escolha = str(input('Escolha uma dessas conversões: binário, octal ou hexadecimal: '))

if escolha.lower() == 'binario' or 'binário':
    str = bin(num)
    print(f'O número {num} em binário vale {str[2:]}')

elif escolha.lower() == 'octal':
    str = oct(num)
    print(f'O número {num} em octal vale {str[2:]}')

else:
    print('EROO -- Insira uma opção válida!')