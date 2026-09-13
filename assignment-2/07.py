# Q.7) Write a program in Python to take a number from user and find its square root and display its binary, hex and octal equivalent.

import math

num = int(input("Enter a number: "))

print("Square root:", math.sqrt(num))
print("Binary equivalent:", bin(num))
print("Hexadecimal equivalent:", hex(num))
print("Octal equivalent:", oct(num))