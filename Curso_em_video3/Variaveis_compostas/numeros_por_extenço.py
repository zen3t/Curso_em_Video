
numeros = ('zero','um','dois','trez','quatro','cinco','seis','sete')
while True:
    num = int(input('Digite um numero entre 0 a 20:  '))
    if num >= 0 and num <= 20:
        break
    print('O numero que voce digitou nao esta na lista. Tente novamente..')
print(f'Digite um numero : {numeros[num]}')
