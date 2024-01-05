def notas(*num, sit=False):
    '''
    -> Função para analisar notas da turma e determinar a situação
    :param num: recebe uma ou mais notas de alunos (aceita várias)
    :param sit: valor opcional, indicando a situação da turma
    :return: retorna dicionário com informações da turma como, maior nota, menor nota, média e situação
    '''
    boletim = dict()
    cont = soma = maior = menor = 0
    for n in num:
        if cont == 0 or n < menor:
            menor = n
        if n > maior:
            maior = n
        soma += n
        cont += 1
    boletim = {'Quantidade de notas': len(num),
               'Maior nota': maior,
               'Menor nota': menor,
               'Média da turma': soma/len(num)}
    if sit == True:
        if boletim['Média da turma'] > 6:
            boletim['Situação'] = 'Boa'
        else:
            boletim['Situação'] = 'Ruim'
    return boletim

resp = notas(7, 9.5, 10, 8.5, 10, 10, sit=True)
print(resp)
print(help(notas))