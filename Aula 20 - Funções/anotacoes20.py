# Todas funções vem acompanhada de ()

#? Declarar uma função
def mostraLinha(): #* Criando uma rotina
    print('-' * 30)
mostraLinha() #* Chamado da função 
print(f'{"Curso em Vídeo":^30}')
mostraLinha()

#? Parâmetro
def mensagem(msg):  #* É o parâmetro que será recebido
    print('-=' * 15)
    print(f'{msg:^30}')
    print('-=' * 15)
mensagem('SITEMA DE ALUNOS') #* Passando o parâmetro   

def soma(a, b):
    s = a + b
    print(s)
soma(1, 5)

#? Empacotamento de parâmetros
def contador(*num): #* Pega todos parâmetros e joga dentro de num, que é uma tupla
    s = 0
    for n in num: #* Desempacotamento
        s += n
    print(f'A soma dos valores {num} é igual a {s}')
contador(1, 2, 3, 4, 5)

#? Lista como parâmetro
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
valores = [7, 2, 0, 4, 2]
dobra(valores)
print(valores)