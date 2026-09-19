# Write a program to check whether the given character is a digit
# or a character in lowercase or uppercase alphabet.

char = input("Enter a character: ")

if ord(char) >= 48 and ord(char) <= 57:
    print("It is a digit.")
elif ord(char) >= 97 and ord(char) <= 122:
    print("It is a lowercase character.")
elif ord(char) >= 65 and ord(char) <= 90:
    print("It is an uppercase character.")
else:
    print("Invalid character.")
