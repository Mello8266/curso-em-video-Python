def maior(*num):
    print('-=' * 15)
    print('Analisando os valores...')
    if len(num) > 0:
        for c in num:
            print(c, end=' ')
        print(f'Foram informados {len(num)} valores ao todo')
        print(f'O maior valor foi o {max(num)}')
    else:
        print('Não foi informado nenhum valor.')

maior(4, 2, 1, 6, 8)
maior(83, 71, 43, 38, 60, 17)
maior()