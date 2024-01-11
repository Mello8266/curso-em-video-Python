import urllib.request

try:
    site = urllib.request.urlopen('https://pudim.com.br/')
except urllib.request.URLerror:
    print('Não está acessível')
else:
    print('Consegui acessar o site')
