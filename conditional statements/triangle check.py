#Write a program that accepts three sides of a triangle and determines whether it is
#equilateral, isosceles, scalene, or not a valid triangle at all.

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

# Check if the triangle is valid
if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Not a valid triangle.")
elif a == b == c:
    print("Equilateral triangle.")
elif a == b or b == c or a == c:
    print("Isosceles triangle.")
else:
    print("Scalene triangle.")

    
#Enter the first side: 4
#Enter the second side: 5
#Enter the third side: 5
#Isosceles triangle.
