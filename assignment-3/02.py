# Write a program that accepts a lowercase/uppercase character
# from the user and checks whether the character is a vowel or consonant.

char = input("Enter the character: ").lower()

if ord(char) >= 97 and ord(char) <= 122:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        print("Character is a vowel.")
    else:
        print("Character is a consonant.")
else:
    print("Invalid input.")
