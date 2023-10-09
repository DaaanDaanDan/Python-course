
def campeonato():
    print ("**** Rodada 1 ****")
    
    partida()

    print ("**** Rodada 2 ****")

    partida()

    print ("**** Rodada 3 ****")

    partida()

    print ("**** Final do campeonato! ****")
    print ("Placar: Você 0 X 3 Computador")

def computador_escolhe_jogada(n, m):
    if n == 1:
        n = 0
        print ("O computador tirou 1 peça")
    
    else:
        tiradas = n
        while (n % (m+1)) != 0:
            n -= 1
        tiradas = tiradas - n
        if (n % (m+1)) == 0 and tiradas > m:
            tiradas = m
            n = n - m
          
        print ("O computador tirou", tiradas, "peça(s).")
        print ("Agora restam", n,"peça(s) no tabuleiro.")
    return n


def usuario_escolhe_jogada(n, m):
    tiradas = int(input("Quantas peças você vai tirar? "))
    while n > 1 and (tiradas > m or tiradas <= 0):
        print ("Oops! Jogada inválida! Tente de novo.")
        tiradas = int(input("Quantas peças você vai tirar? "))

    print ("Você tirou", tiradas, "peça(s).")
    n = n - tiradas
    print ("Agora restam", n,"peça(s) no tabuleiro.")
    return n

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if (n % (m+1) == 0):
        print ("Você começa!")
        while n > 0:
            n = usuario_escolhe_jogada(n, m)
            if n > 0:
                n = computador_escolhe_jogada(n, m)
        print ("Fim do jogo! O computador ganhou!")
            

    else:
        print ("Computador começa!")
        while n > 0:
            n = computador_escolhe_jogada(n, m)
            if n > 0:
                n = usuario_escolhe_jogada(n, m)
        print ("Fim do jogo! O computador ganhou!")
                    

print ("Bem-vindo ao jogo do NIM! Escolha: ")

print ("1 - para jogar uma partida isolada")
print ("2 - para jogar um campeonato")

tipo = int(input())
if tipo == 1:
    print ("Voce escolheu uma partida isolada!")

    partida()
if tipo == 2:
    print ("Voce escolheu um campeonato!")

    campeonato()
