c = 'limite de velocidade 80km'.upper()
print(f'{c:=^50}')
velocidade = int(input('digite a velocidade :'))
if velocidade > 80:
    multa = ((velocidade - 80) * 7)
    print(f'Voce estava ha {velocidade}km\nVoce foi multado com :{multa}R$')
else:
    print(f'nao foi multado voce estava a {velocidade}km por hora !')
