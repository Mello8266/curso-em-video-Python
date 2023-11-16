print('Conversão númerica')
num = int(input('Isira um número inteiro: '))
escolha = str(input('Escolha uma dessas conversões: binário, octal ou hexadecimal: ')).lower()

if escolha == 'binario' or 'binário':
    str = bin(num)
    print(f'O número {num} em binário vale {str[2:]}')

elif escolha == 'octal':
    str = oct(num)
    print(f'O número {num} em octal vale {str[2:]}')

elif escolha == 'hexadecimal':
    string = hex(num)
    print(f'O número {num} em hexadecimal vale {string[2:]}')

else:
    print('EROO -- Insira uma opção válida!')