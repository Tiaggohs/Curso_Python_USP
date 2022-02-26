print ("Type a natural number: ")
n = int(input())
fact = n
factFinal = 1

if (n == 0):
    fact = 1
    n = 0
    
while (n > 2):
    fact = fact * (n-1)
    n = n - 1

print (fact)