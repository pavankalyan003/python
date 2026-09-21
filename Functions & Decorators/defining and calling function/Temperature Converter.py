def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


while True:
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        c = float(input("Enter Celsius: "))
        f = celsius_to_fahrenheit(c)
        print("Fahrenheit:", f)

    elif choice == 2:
        f = float(input("Enter Fahrenheit: "))
        c = fahrenheit_to_celsius(f)
        print("Celsius:", c)

    elif choice == 3:
        print("Program ended.")
        break

    else:
        print("Invalid choice")


'''
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Exit
Enter your choice: 1
Enter Celsius: 45
Fahrenheit: 113.0

1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Exit
Enter your choice: 2
Enter Fahrenheit: 113
Celsius: 45.0

1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Exit
Enter your choice: 3
Program ended.
'''
