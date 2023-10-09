import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def caracteres(frase):
    soma_caracteres = 0
    contador = 0
    while contador <= len(frase):
        soma_caracteres += len(frase[contador])
        contador += 1
    return soma_caracteres



def compara_assinatura(as_a, as_b):
    
    soma_temp = 0
    for i in range(0,6):
        soma_temp = soma_temp + (abs(as_a[i] - as_b[i]))
    
    return soma_temp / 6  

def calcula_assinatura(texto):
    
    frases = []
    palavras = []
    sentencas = separa_sentencas(texto)
    soma_car_sentenca = 0 
    soma_car_frases = 0
    soma_pal = 0
    tam_med_pal = 0
    tam_med_sent = 0
    complex_sent = 0
    rel_type_token = 0
    hapax = 0
    tam_med_fra = 0

    for sentenca in sentencas:
        soma_car_sentenca += len(sentenca)
        lista_frases = separa_frases(sentenca)

        for f in lista_frases:
            frases.append(f)

    for frase in frases:
        soma_car_frases += len(frase)
        lista_pal = separa_palavras(frase)

        for palavra in lista_pal:
            palavras.append(palavra)

    for palavra in palavras:
        soma_pal += len(palavra)

    tam_med_pal = soma_pal / len(palavras)
    rel_type_token = n_palavras_diferentes(palavras) / len(palavras)
    hapax = n_palavras_unicas(palavras) / len(palavras)
    tam_med_sent = soma_car_sentenca / len(sentencas)
    complex_sent = len(frases) / len(sentencas)
    tam_med_fra = soma_car_frases / len(frases)
    
    return [tam_med_pal, rel_type_token, hapax, tam_med_sent, complex_sent, tam_med_fra]

def avalia_textos(textos, ass_cp):
    inf = []
    
    for texto in textos:
        ass_texto = calcula_assinatura(texto)
        inf.append(compara_assinatura(ass_texto, ass_cp))

    menor = inf[0]
    c = 1

    for i in range(1, len(inf)):
        if (menor > inf[i]):
            c = i
    return c

def main():        
    assinatura = le_assinatura()
    textos = le_textos()
    x = avalia_textos(textos, assinatura)
    print(f"O autor do texto {x} está infectado com COH-PIAH")

main()

