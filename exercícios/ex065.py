soma = 0
count = 1
while True:
    n = int(input(f'Insira o {count}º valor: '))
    soma += n
    count += 1
    if count == 2:
        maior = n
        menor = n

    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    para = str(input('Deseja parar a aplicação? [S/N] ')).upper()
    if para in ('S, SIM, S'):
        break
media = soma / count
print(f'A soma dos valores digitados é: {soma} \nA média dos valores é: {media} \nO maior valor é: {maior} e o menor: {menor}')