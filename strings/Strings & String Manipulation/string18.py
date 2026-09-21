s = input("Enter a sentence: ")

words = s.split()
result = []

for word in words:
    result.append(word[0].upper() + word[1:].lower())

print("Title Case:", " ".join(result))


'''
Enter a sentence: python is easy 
Title Case: Python Is Easy
'''
