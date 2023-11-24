f = str(input('Insira uma frase e veja se ela é um palindromo: ')).strip()
f2 = f.replace(' ', '').upper()
fin = f2[::-1]

if f2 == fin:
    print(f'É um palindromo!')

else:
    print('Não é um palindromo')

print(f'Frase: "{f}" \nInverso: "{fin}"')