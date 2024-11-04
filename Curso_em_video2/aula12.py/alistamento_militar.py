from datetime import date
ano_atual = date.today().year
print('Idade para o alistamento e de 18 anos ..!')

seu_ano = int(input('Digite o ano de nascimento: '))

alistamento = ano_atual - seu_ano
print(f'Quem nasceu em {seu_ano} tem {alistamento} anos em {ano_atual}')

if alistamento == 18:
    print(f'Estamos {ano_atual} voçe esta com {alistamento} anos está na hora do alistamento ..')
elif alistamento < 18:
    saldo = 18 - alistamento
    ano = ano_atual + saldo
    print(f'Voçe está com {alistamento} de idade deve se alistar em {ano }  ..!')
elif alistamento > 18:
    saldo = alistamento - 18
    ano = ano_atual - saldo
    print(f'Voçe esta com {alistamento} deveria ter se alistado em {ano} ..!')

