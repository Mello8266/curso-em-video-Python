frase = ('xicara', 'cafe', 'boneco', 'estudar', 'python', 'emprego', 'futuro', 'programador')

# Minha maneira - muito extensa
for c in frase:
    a = c.find('a')
    e = c.find('e')
    i = c.find('i')
    o = c.find('o')
    u = c.find('u')
    print(f'\nNa palavra {c.upper()} temos: ', end='')
    if a > 0:
        print(f'{c[a]}', end=' ')
    if e > 0:
        print(f'{c[e]}', end=' ')
    if i > 0:
        print(f'{c[i]}', end=' ')
    if o > 0:
        print(f'{c[o]}', end=' ')
    if u > 0:
        print(f'{c[u]}', end=' ')

# Maneira menor
for i in frase:
    print(f'\nNa palavra {i.upper()} temos: ', end='')
    for letra in i:
        if letra in 'aeiou':
            print(f'{letra}', end='')