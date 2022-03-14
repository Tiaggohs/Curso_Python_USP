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

def remove_punctuation(text):
    '''NEW FUNCTION. This function receive a text and return a new text without punctuation. '''
    listOfSentences = separa_sentencas(text)
    concatElements = ""
    for x in range(len(listOfSentences)):
        concatElements = concatElements + listOfSentences[x]
    listOfPhrases = separa_frases(concatElements)
    concatElements2 = ""
    for x in range(len(listOfPhrases)):
        concatElements2 = concatElements2 + listOfPhrases[x]

    return concatElements2

def calculeAverage(text):
    '''NEW FUNCTION. This function receive a text without punctuation and return the avearage of letter for words. '''
    finalListOfWords = separa_palavras(remove_punctuation(text))
    sumOfLetters = 0
    sumOfWords = 0
    for x in range(len(finalListOfWords)):
        sumOfLetters = sumOfLetters + len(finalListOfWords[x])
        sumOfWords = sumOfWords + 1
    average = sumOfLetters / sumOfWords

    return average

def calculeTypeToken(text):
    '''NEW FUNCTION. This function receive a text and calcule the division between the number of diferent words and the number of words. '''
    totalOfWords = len(separa_palavras(remove_punctuation(text)))
    totalOfDifferentWords = n_palavras_diferentes(separa_palavras(remove_punctuation(text.lower())))

    return totalOfDifferentWords / totalOfWords

def calculeHapaxLegomana(text):
    '''NEW FUNCTION. This function receive a text and calcule the division between the number of unic words and the number of words. '''
    totalOfWords = len(separa_palavras(remove_punctuation(text)))
    totalOfUnicWords = n_palavras_unicas(separa_palavras(remove_punctuation(text.lower())))

    return totalOfUnicWords / totalOfWords

def average_sizaSentence(text):
    '''NEW FUNCTION. This function receive a text and calcule the average of caracters for sentence. '''
    totalOfSentences = len(separa_sentencas(text))
    sumOfCaracters = 0
    listWithoutSpace = separa_sentencas(text)
    for x in range(len(listWithoutSpace)):
        sumOfCaracters = sumOfCaracters + len(listWithoutSpace[x])
    
    return sumOfCaracters / totalOfSentences

def coplexityOfSentence(text):
    '''NEW FUNCTION. This function receive a text and calcule the division between the number of phases and the number of sentences. '''
    listOfSentences = separa_sentencas(text)
    qtyOfPhrases = 0
    for x in range(len(listOfSentences)):
        qtyOfPhrases = qtyOfPhrases + len(separa_frases(listOfSentences[x]))
    
    return qtyOfPhrases / len(listOfSentences)

def sizeAveragePhases(text):
    '''NEW FUNCTION. This function receive a text and calcule the average of letters for phrases. '''
    listOfSentences = separa_sentencas(text)
    listOfPhrases = []
    qtyOfPhrases = 0
    qtyOfLetters = 0
    for x in range(len(listOfSentences)):
        qtyOfPhrases = qtyOfPhrases + len(separa_frases(listOfSentences[x]))
        auxList = separa_frases(listOfSentences[x])
        for x in range(len(auxList)):
            qtyOfLetters = qtyOfLetters + len(auxList[x])
        
    return qtyOfLetters / qtyOfPhrases

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    summation = 0
    for x in range(len(as_a)):
        summation = summation + abs(as_a[x] - as_b[x])

    return summation / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    wal = calculeAverage(texto)
    ttr = calculeTypeToken(texto)
    hlr = calculeHapaxLegomana(texto)
    sal = average_sizaSentence(texto)
    sac = coplexityOfSentence(texto)
    pal = sizeAveragePhases(texto)
    
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    listOfSummations = []
    n = 0
    for x in range(len(textos)):
        listOfSummations.append(compara_assinatura(calcula_assinatura(textos[x]), ass_cp))
    for x in range(len(listOfSummations)-1):
        if listOfSummations[x] < listOfSummations[x - 1]:
            n = x

    return n + 1

avalia_textos(le_textos(), le_assinatura())
