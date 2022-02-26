print ("Type the first number to put in ascending order: ")
num1 = int(input())

print ("Type the second number to put in ascending order: ")
num2 = int(input())

print ("Type the third number to put in ascending order: ")
num3 = int(input())

first = 0
second = 0
third = 0

if (num1 > num2 and num1 > num3):
    third = num1
else:
    if num1 < num2 and num1 < num3:
        first = num1
    else:
        second = num1

if (num2 > num1 and num2 > num3):
    third = num2
else:
    if num2 < num1 and num2 < num3:
        first = num2
    else:
        second = num2

if (num3 > num1 and num3 > num2):
    third = num3
else:
    if num3 < num2 and num3 < num2:
        first = num3
    else:
        second = num3

print (str(first) + ", " + str(second) + ", " + str(third))