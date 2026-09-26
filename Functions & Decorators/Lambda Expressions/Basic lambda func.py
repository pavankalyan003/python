# Square of a number
square = lambda x: x * x

# Check whether number is even
even = lambda x: x % 2 == 0

# Find larger number
larger = lambda x, y: x if x > y else y


n = int(input("Enter a number: "))
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Square =", square(n))
print("Is even =", even(n))
print("Larger number =", larger(a, b))


'''
Enter a number: 14
Enter first number: 45
Enter second number: 35
Square = 196
Is even = True
Larger number = 45
'''
