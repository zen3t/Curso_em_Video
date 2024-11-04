c = 'media dos alunos'.upper()
print(f'{c:=^50}')
nota1 = float(input('Diagite uma nota: '))
nota2 = float(input('Diagite outra nota: '))
media = (nota1 + nota2) / 2 
if media <= 5.0:
    print(f'A sua e media e: {media}\nVoce esta REPROVADO ...!')
elif media <= 6.9:
    print(f'A sua media e de {media} voce esta em RECUPERACAO ...!')
else:
   
    print(f'{media} APROVADO ..')
