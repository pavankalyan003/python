# Write a program to print all prime numbers between two given limits.
start = int(input("Enter the lower limit: "))
end = int(input("Enter the upper limit: "))

print("Prime numbers:")

for num in range(start, end + 1):
    if num < 2:
        continue

    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, end=" ")



#output:
#Enter the lower limit: 2
#Enter the upper limit: 99
#Prime numbers:
#2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
