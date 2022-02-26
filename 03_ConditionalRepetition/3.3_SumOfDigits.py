print ("Type a natural integer number: ")
n = int(input())

sum = 0
numToSum = 0

while (n > 0):
    numToSum = n % 10
    n = n //10
    sum = numToSum + sum

print (sum)
    