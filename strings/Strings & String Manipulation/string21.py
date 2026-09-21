s = input("Enter a string: ")

if s.isdigit():
    print("Contains only digits")
elif s.isalpha():
    print("Contains only alphabets")
elif s.isalnum():
    print("Contains alphabets and digits")
else:
    print("Contains special characters")


'''
Enter a string: pavan123
Contains alphabets and digits
'''
