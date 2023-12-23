# alunos [nome[notas]]
alunos = list()
nome = list()
notas = list()

while True:
    nome.append(str(input('Nome do aluno: ')).strip().capitalize())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    nome.append(notas[:])
    alunos.append(nome[:])
    if len(notas) == 2:
        notas.clear()
        nome.clear()
    conf = str(input('Deseja continuar? ')).strip().upper()[0]
    if conf in 'N':
        break
print(f'\n{"Nº":3} {"NOME":<15} {"MÉDIA"}')
print('-' * 25)

n = 0
for c in alunos:
    print(f'{n:<3} {c[0]:<15} {sum(c[1]) / len(c[1]):>4.1f}',end='\n')
    n += 1
print('-' * 25)

while True:
    n = int(input('Deseja visualizar a nota de qual alunos? (-1 interrompe) Nº'))
    if n != -1:
        print(f'Notas de {alunos[n][0]} são: {alunos[n][1]}\n')
    else:
        break
print('Fim do programa')