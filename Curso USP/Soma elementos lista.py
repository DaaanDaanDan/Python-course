lista = [1,2,3,4,5,6,0,10]

def soma_elementos(lista):
    soma = 0
    cont = 0
    while cont <= (len(lista)-1):
        soma = soma + lista[cont]
        cont += 1
    return soma
