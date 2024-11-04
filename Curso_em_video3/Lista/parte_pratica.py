# num = [1,2,4,3,7,6]
# num[3] = 9
# num.sort(reverse=True)
# num.pop(2)
# num.append(8)
# num.insert(3,2)
# num.remove(2)
# num[:3]
# print(num)
# print(f'Essa lista tem {len(num)}')
num = []
for cont in range(0,5):
    num.append(int(input('Digite um numero: ')))
for c,v in enumerate(num):
    print(f'na posicao {c} encotrei o valor {v}')
#
# a = [2,3,1,5,7]
# b = a[:]
#
# b[2] = 8
# print(f'A lista A {a}')
# print(f'Uma copia de a {b}')
