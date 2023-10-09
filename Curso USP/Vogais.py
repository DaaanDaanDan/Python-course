def vogal(x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return True
    return False

a = input("Digite um caralho? ").lower()

print (vogal(a))