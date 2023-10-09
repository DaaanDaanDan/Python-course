def ePrimo(x):
    fator = 2
    while x % fator != 0 and fator < (x - 1):
        fator += 1
    if x % fator == 0:
        return False
    if x == 2:
        return True
    else:
        return True


def n_primos(n):
    soma = 0
    while n > 0:
        if ePrimo(n) == True:
            soma += 1
        n -= 1
    return soma

teste = n_primos(121)

print (teste)

