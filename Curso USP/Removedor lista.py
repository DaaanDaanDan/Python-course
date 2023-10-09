

def remove_repetidos(lista):
    lista.sort()
    x = 0
    y = 1
    while y < (len(lista)):
        if lista[x] == lista[y]:
            del lista[x]
        else:
            x += 1
            y += 1
    return lista