s = input("Enter a string: ")

result = ""

for ch in s:
    if ch.isupper():
        result += ch.lower()
    elif ch.islower():
        result += ch.upper()
    else:
        result += ch

print("Swapped case:", result)

'''
Enter a string: PAvan
Swapped case: paVAN
'''
