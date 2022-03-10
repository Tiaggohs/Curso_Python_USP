def maior_elemento(list):

    newList = sorted(list)
    
    return newList[-1]


testList = [3, 4, 7, 7, 3, 10, 13, 10, 3, 2]

print(maior_elemento(testList))
