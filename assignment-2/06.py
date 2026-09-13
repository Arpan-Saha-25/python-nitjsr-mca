# Q.6) Write a program in Python to left, right and centered justify a string.

text = input("Enter a string: ")

width = 30

print("Left justified  :", text.ljust(width))
print("Right justified :", text.rjust(width))
print("Centered        :", text.center(width))