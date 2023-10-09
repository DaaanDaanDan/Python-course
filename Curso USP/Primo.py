x = int(input("Digite um número inteiro: "))

cont = 2
primo = True

while (cont < x and primo):

    primo = not ((x % cont) == 0)
    cont += 1


if (primo):
    print("primo")
else:
    print("não primo")