#Write a program to find the largest of three numbers using nested if-else
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b:
    if a >= c:
        largest = a
    else:
        largest = c
else:
    if b >= c:
        largest = b
    else:
        largest = c

print("The largest number is:", largest)


#Enter first number: 54
#Enter second number: 56
#Enter third number: 7
#The largest number is: 56.0
