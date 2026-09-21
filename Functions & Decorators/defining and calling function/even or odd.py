def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

for i in range(5):
    n = int(input("Enter a number: "))

    if is_even(n):
        print(n, "is Even")
    else:
        print(n, "is Odd")


'''      
Enter a number: 10
10 is Even
Enter a number: 3
3 is Odd
Enter a number: 23
23 is Odd
Enter a number: 4
4 is Even
Enter a number: 5
5 is Odd
'''
