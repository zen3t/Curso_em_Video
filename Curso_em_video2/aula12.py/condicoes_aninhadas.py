from time import sleep
nome = str(input('Dgite o seu nome: ')).strip().capitalize()
if nome == 'Zeneto':
    print('Analizando .....')
    sleep(3)
    print(f'{nome} pode entrar ...\nSeja bem vindo ..')
elif nome != 'Zeneto':
    print('Analizando .....')
    sleep(3)
    print(f'O bom dia {nome} voce nao esta cadastrado! ')
