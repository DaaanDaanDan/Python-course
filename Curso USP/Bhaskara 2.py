import math

a = int(input("Digite o a da equiação: "))

b = int(input("Digite o b da equiação: "))
              
c  =int(input("Digite o c da equiação: "))

delta = (b**2) - (4*a*c)

if delta > 0:

    x1 = ((-b) + (math.sqrt(delta)))/ (2*a)

    x2 = ((-b) - (math.sqrt(delta)))/ (2*a)

    if (x1 < x2):

        print ("As raízes são", x1, "e", x2)

    else:

        print ("As raízes são", x2, "e", x1)

    

if delta == 0:

    x3 = ((-b) / (2*a))

    print ("A raíz é", x3)

if delta < 0:
    
    print ("A expressão não tem raíz real")