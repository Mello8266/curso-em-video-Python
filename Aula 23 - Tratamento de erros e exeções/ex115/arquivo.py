from interface import *

def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Ocorreu um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        titulo('PESSOAS CADASTRAD AS')
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<42}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um problema ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao tentar escrever no arquivo')
        else:
            print(f'{nome} registrado na base de dados')
        finally:
            a.close()
