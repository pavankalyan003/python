#Write a program to check whether a character entered by the user is a vowel, consonant,
#digit, or special symbol.
ch = input("Enter a character: ")

if ch.isalpha():
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("Special symbol")
#Enter a character: 4
#Digit
