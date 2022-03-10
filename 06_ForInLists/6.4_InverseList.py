num1 = -1
InputList = []
aux = -2

while num1 != 0:    
    print ("Digite um número: ")
    num1 = int(input())
    InputList.append(num1)

for x in range(len(InputList)-1):
    print (InputList[aux])
    aux = aux - 1
