from datetime import date

def voto(ano):
    ano_atual = date.today().year 
    idade = ano_atual - ano
    if idade < 16:
        return f'Com {idade} nao vota'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} o voto é opcional'
    else:
        return f'Com {idade} O voto é Obrigatorio'


pessoa = int(input('Digite o seu ano de nascimento: '))
print(voto(pessoa))
