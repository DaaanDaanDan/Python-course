n = int(input("Digite um número: "))
while n >= 0:
    
    fat = 1

    while (n > 0):

        fat = fat * n

        n = n - 1
        
    print (fat)  
    n = int(input("Digite um número: "))