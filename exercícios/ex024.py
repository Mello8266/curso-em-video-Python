cidade = str(input('Insira o nome da sua cidade: ')).strip()

if cidade[:5].lower().find('santo') == 0:
    print('Sua cidade começa com a palavra santo')

else:
    print('Sua cidade não começa com a palavra santo')