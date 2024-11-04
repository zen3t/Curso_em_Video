c = 'loja do ze'.upper()
print(f'{c:=^50}')
preco_produto = float(input('Qual é o preco do produto: '))
avistaDinheiro = preco_produto - (preco_produto * 10 / 100)
avistaCartao = preco_produto - (preco_produto * 5 / 100)
tres_no_cartao = preco_produto + (preco_produto * 20 / 100)
escolha = int(input(
        '''
        1=) A vista com dinheiro ou cheque 10% de desconto
        2=) A vista no cartao 5% de desconto
        3=) Em ate 2x no cartao preco normal
        4=) Em ate 3x no cartao 20% de juros
        escolha de 1 ate 4 : 
        '''
        ))
print(f'Sua opcao foi : {escolha}')
if escolha == 1:
    print(f'Sua compra de R$: {preco_produto} vai custar R$: {avistaDinheiro:.1f}')
elif escolha == 2:
    print(f'Sua compra de R$:{preco_produto} vai custar R$: {avistaCartao:.1f}')
elif escolha == 3:
    parcela = preco_produto / 2
    print(f'Sua compra vai ser parcelada e 2X de R$: {parcela}')
    print(f'Sua compra de R$:{preco_produto} vai custar R$: {preco_produto} no final')

elif escolha == 4:
    totalpar = int(input('Quantas parcelas: '))
    parcela = tres_no_cartao / totalpar
    print(f'Sua compra de R$:{preco_produto} vai custar R$: {tres_no_cartao}R$')
    print(f'Sua compra vai ser parcelada e 3X de R$: {parcela:.1f}')
else:
    escolha = preco_produto
    print('Opcao invalida de pagamento')
