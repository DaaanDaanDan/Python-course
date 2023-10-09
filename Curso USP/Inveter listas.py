lista = []
x = 1

while x != 0:
    x = int(input("Digite um número para adicionar na lista e zero para finalizar: "))
    if x != 0:
        lista.append(x)

tam = len(lista) - 1
    
while tam >= 0:
    if tam != 0:
        print (lista[tam])
        tam -= 1
    else:
        print (lista[tam])
        tam -= 1
        