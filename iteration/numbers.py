#Write a program to print the first N natural numbers using a while loop.

N = int(input("enter number:"))
i = 1

print(f"The first {N} natural numbers are:")
while i <= N:
    print(i, end=" ")
    i += 1
print()


#enter number:9
#The first 9 natural numbers are:
#1 2 3 4 5 6 7 8 9 
