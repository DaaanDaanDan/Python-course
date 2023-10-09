x = int(input("Digite um número: "))
fat = 1

if x == 0:
    print ("1")
else:
    while (x > 0):

        fat = fat * x

        x = x - 1
    print (fat)


