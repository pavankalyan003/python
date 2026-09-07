s = input("Enter a sentence: ")

words = s.split()

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)


'''
Enter a sentence: python is easy language
Longest word: language
'''
