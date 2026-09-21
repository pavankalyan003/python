s = input("Enter a string: ")
sub = input("Enter substring: ")

# Find first occurrence
first = -1

for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        first = i
        break

# Count occurrences
count = 0

for i in range(len(s) - len(sub) + 1):
    if s[i:i + len(sub)] == sub:
        count += 1

print("First occurrence index:", first)
print("Number of occurrences:", count)


'''
Enter a string: python
Enter substring: on
First occurrence index: 4
Number of occurrences: 1
'''
