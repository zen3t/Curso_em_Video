
while True:
    n = int(input('digite o numero para a sua tabuada: '))   

    if n < 0:
            
        break
    for i in range(1,11):
        
        print(f'{n} x {i:2} = {i*n}')
print('fimm')        
