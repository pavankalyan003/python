s = input("Enter a string: ")
ch = input("Enter character: ")

first = s.find(ch)
last = s.rfind(ch)

print("First occurrence:", first)
print("Last occurrence:", last)

'''
Enter a string: kalyan
Enter character: a
First occurrence: 1
Last occurrence: 4
'''
