print('Qual a quantidade de tinta necessária para pintar sua parede?')

a = float(input('Altura da parede? '))
l = float(input('Largura da parede? '))

area = a * l
tinta = area/2

print('A área da sua parede é {}m²'.format(area))
print('Quantidade de tinta necessária {}l'.format(tinta))