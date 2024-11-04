total = 0
n = int(input('digite um numero: '))
for i in range(1,n+1):
    if n % i == 0:
        print('\033[33m',end='')
        total += 1
    else:
        print('\033[31m',end='')
    print(f'{i}')
print(f'\n\033[mO numero {n} foi divisivel {total} vezes')

if total == 2:
    print('Por isso ele é PRIMO')
else:
    print('Por isso ele nao e PRIMO')
