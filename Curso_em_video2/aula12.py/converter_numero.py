numero = int(input('Digite um numero: '))
binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)
escolha = input('''
                1 =) BINARIO 
                2 =) OCTAL 
                3 =) HEXADECIMAL
                >>> 
                ''')
if escolha == '1':
    print(f'Binario: {binario[2:]}')

elif escolha == '2':
    print(f'Octal: {octal[2:]}')
elif escolha == '3':
    print(f'Hexadecimal: {hexadecimal[2:]}')
else:
    print('Opcao invalida tente novamente')
