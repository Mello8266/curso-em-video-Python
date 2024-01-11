from arquivo import *
from interface import *
from time import sleep

arq = 'basedadoex115.txt'

if not arqExiste(arq):
    criarArq(arq)

while True:
    print()
    titulo('MENU PRINCIPAL')
    sleep(0.5)

    esco = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Encerrar programa'])
    if esco == 1:
        lerArquivo(arq)
    elif esco == 2:
        titulo('NOVO CADASTRO')
        nome = str(input('Nome: ')).strip().capitalize()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif esco == 3:
        break
    else:
        print(f'{cor("vermelho")}ERRO! Digite uma opção válida. {cor("limpa")}')     
    sleep(2)
print('Fim do programa!')
