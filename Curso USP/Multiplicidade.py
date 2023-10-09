x = int(input("Digite um número inteiro > 1: "))
fator = 2
mult = 0 

while x > 1:

    while x % fator == 0:
        mult = mult + 1
        x = x / fator

    if mult > 0:
        print ("Fator", fator, "multiplicidade = ", mult)
    fator = fator + 1
    mult = 0