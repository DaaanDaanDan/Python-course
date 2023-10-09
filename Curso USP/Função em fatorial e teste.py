def fatorial(x):
    fatorial = 1
    while (x > 1):
        fatorial = fatorial * x
        x = x - 1
    return fatorial

def numero_binomial(n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n-k))

def teste_fatorial():
    if fatorial(1) == 1:
        print ("Funciona para 1")
    else:
        print ("Não funciona para 1")
    if fatorial(2) == 2:
        print ("Funciona para 2")
    else:
        print ("Não funciona para 2")
    if fatorial(5) == 120:
        print ("Funciona para 5")
    else:
        print ("Não funciona para 5")
    if fatorial(0) == 1:
        print ("Funciona para 0")
    else:
        print ("Não funciona para 0")

bala = numero_binomial(20, 10)

print (bala)
