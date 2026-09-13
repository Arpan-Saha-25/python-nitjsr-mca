# Q.9) Write a program in Python to find the character values for different numbers and ASCII value for different characters.

# Character values for different numbers
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print("Character for", num1, ":", chr(num1))
print("Character for", num2, ":", chr(num2))

# ASCII values for different characters
char1 = input("Enter a character: ")
char2 = input("Enter another character: ")
print("ASCII value of", char1, ":", ord(char1))
print("ASCII value of", char2, ":", ord(char2))