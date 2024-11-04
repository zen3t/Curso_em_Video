sexo = str(input('Informe o seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados, Invalidos por favor Informe o seu sexo :')).strip().upper()[0]
print(f'O sexo registrado consucesso {sexo}')
