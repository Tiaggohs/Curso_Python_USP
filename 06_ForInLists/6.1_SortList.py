def remove_repetidos(list):

    newList = sorted(list)
    finalList = []
    
    for x in range(len(newList)):
        if newList[x] != newList[x-1]:
            finalList.append(newList[x])

    return finalList
    'return newList'


testList = [3, 4, 7, 7, 3, 10, 13, 10, 3, 2]

print(remove_repetidos(testList))
