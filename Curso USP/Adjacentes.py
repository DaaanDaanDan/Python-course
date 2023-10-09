x = int(input("Digite um número: "))

adj = False

while (x > 0) and (adj == False):

    d = x % 10

    x = x // 10

    e = x % 10

    if d == e:
        adj = True
    else:
        adj = False

if adj == True:

    print ("Existem dois números adjacentes")

else:

    print ("Não existem dois números adjacentes")