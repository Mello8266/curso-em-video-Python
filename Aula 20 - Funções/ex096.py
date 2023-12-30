def area():
    l = float(input('Largura: (m) '))
    c = float(input('Comprimento: (m) '))
    area = l * c
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {area}m²')
area()