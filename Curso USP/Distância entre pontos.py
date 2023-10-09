import math

x1 = int(input("Digite o primeiro x: "))

y1 = int(input("Digite o primeiro y: "))

x2 = int(input("Digite o segundo x: "))

y2 = int(input("Digite o segundo y: "))

distancia = math.sqrt (((x1 - x2)**2) + ((y1 - y2)**2))

if distancia >= 10:

    print ("Longe")

else:
    
    print ("perto")