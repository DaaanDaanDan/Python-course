x = int(input("Digite um número: "))

soma = 0

while (x > 0):

    separado = x % 10

    x = x // 10

    soma = separado + soma

print ("A soma dos dígitos é>: ", soma)