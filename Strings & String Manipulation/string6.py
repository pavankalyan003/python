
s = input("Enter a string: ")
ch = input("Enter character to count: ")

count = 0

for x in s:
    if x == ch:
        count += 1

print("Occurrences:", count)


'''
output:
Enter a string: pavan
Enter character to count: a
Occurrences: 2
'''
