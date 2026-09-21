s = input("Enter a string: ")

result = ""

for ch in s:
    if not ch.isspace():
        result += ch

print("After removing whitespace:", result)


'''
output:
Enter a string: p a van
After removing whitespace: pavan
'''
