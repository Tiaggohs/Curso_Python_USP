print ("Type a number to verify: ")
num1 = int(input())

if (num1%3 == 0 and num1%5 == 0):
    print ("FizzBuzz")
else:
    print (num1)