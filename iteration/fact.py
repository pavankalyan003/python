#Write a program to find the factorial of a given number using a for loop.
num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial =", factorial)



#output:
#Enter a number: 15
#Factorial = 1307674368000
