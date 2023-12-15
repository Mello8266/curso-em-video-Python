print('Conversão de metros para centímetros e milimetros')

m = float(input('Insira uma medida em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10 
cm = m * 100
mm = m * 1000

print('A medida de {}m corresponde a {}km, {}hm, {}dam'.format(m, km, hm, dam), end="")
print(', {}dm , {:.0f}cm, {:.0f}mm'.format(dm, cm, mm))