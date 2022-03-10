def soma_elementos(list):

    sumItems = 0
    
    for x in range(len(list)):
        sumItems = sumItems + list[x]

    return sumItems

testList = [3, 4, 7]

print(soma_elementos(testList))
