def maior_primo(x):


    while ((x % 2) == 0) or ((x % 3) == 0) or ((x % 5) == 0) or ((x % 7) == 0):
        x -= 1
    
    return x