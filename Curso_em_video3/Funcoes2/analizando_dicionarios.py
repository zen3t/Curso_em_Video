def notas(*n,sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = len(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media']  <= 5:
             r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r



# progama principal

resp = notas(23.2,4.6,5.6,2.4,6.3)
print(resp)
