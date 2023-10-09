
def eHipotenusa(n: int):
    i = 1
    j = 1
    while i < n:
        if (n**2) == (i**2) + (j**2):
            return n
        while j < n:
            if (n**2) == (i**2) + (j**2):
                return n
            else:   
                j += 1
        i += 1
    

def somaHipotenusas(n):
    fim = n
    while fim >= 1:
        
        eHipotenusa(n)
       
        fim -= 1
        n -= 1

