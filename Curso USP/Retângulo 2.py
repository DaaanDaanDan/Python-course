x = int(input("digite a largura: "))
y = int(input("digite a altura: "))

limitex = x
limitey = y
while y > 0:
    teste = x
    if y == 1 or y == limitey:
        while x > 0:
            print ("#", end = "")
            x -= 1
            
    else:
        while x > 0:

            while x == 1 or x == limitex:
                print ("#", end = "")
                x -= 1
            if x > 1:
                print (" ", end = "")
            x -= 1

    x = teste
    print ()
    y -= 1