x = int(input("digite a largura: "))
y = int(input("digite a altura: "))

while y > 0:
    teste = x
    while x > 0:
        print ("#", end = "")
        x -= 1
    print ("", end = "")
    x -= 1

    x = teste
    print ()
    y -= 1