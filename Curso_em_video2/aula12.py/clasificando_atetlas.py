import datetime
c = 'confederaçao nacional de nataçao'.upper()
print(f'{c:=^50}')

ano_atual = datetime.datetime.now().year
ano_nascimento = int(input('Digite o seu ano de nascimento: '))

idade_atleta = ano_atual - ano_nascimento
print(f'O atleta nasceu em {ano_nascimento}')
if idade_atleta <= 9:
    print(f'IDADE: {idade_atleta} MIRIM !')
#elif idade_atleta > 9 and idade_atleta <= 14:
elif idade_atleta <=14:
    print(f'IDADE: {idade_atleta} INFANTIL !')
#elif idade_atleta > 14 and idade_atleta <= 19:
elif idade_atleta <=19:
    print(f'IDADE: {idade_atleta} JUNIOR !')
#elif idade_atleta > 19 and idade_atleta <= 20:
elif idade_atleta <=25:
    print(f'IDADE: {idade_atleta} SENIOR !')
else:
    print(f'IDADE: {idade_atleta} MASTER !')
