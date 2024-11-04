# funcao de contador
# def contador(i,f,p):
#     c = 1
#     while c <= f:
#         print(f'{c}',end='')
#         c += p
#     print()
# contador(2,10,2)

# # funcao soma
# def soma(a=0,b=0,c=0):
#     s = a + b + c
#     return s
# print(f'A soma dos tres numeros {soma(2,4,5)}')
# print(f'A soma de 2 numeros {soma(2,4)}')
# print(f'A soma de apenas 1 numeros {soma(5)}')


# # Fatorial

def fatorial(num=1):
    f = 1
    for c in range(num, 0 , -1):
        f *= c
    return f


n = int(input('Digite um numero: '))
print(f'O fatorial de um numero é : {fatorial(n,show=True)}')


# def par(n=0):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
# while True:
#     numero = int(input('Escreva um numero: '))
#     if par(numero):
#         print(f'e par')
#     else:
#         print('E impar')
#
#     while True:
#         res = str(input('quer continuar: [S/N]')).upper()[0]
#         if res in 'SN':
#             break
#         print('ERROR responda apenas S ou N')
#     if res == 'N':
#         break
# from datetime import date
# date.today().year
