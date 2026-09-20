# Write a program to convert a binary number to a decimal number without using built-
# in  function  provided  by  Python.  Note  that  you  need  to  check  the  input  is  binary 
# number or not. 
# Sample input and output: 
# Input: Enter a binary number (with 0 and 1's) : 101101 
# Output: The decimal number is 45  
# Input: Enter a binary number (with 0 and 1's) : 103402 
# Output: Invalid input !!!  
# Input: Enter a binary number (with 0 and 1's) : 10001001 
# Output: The decimal number is 137 

binaryNum = input("Enter the binary string: ")

valid = True

for i in binaryNum:
    if i != '0' and i != '1':
        valid = False
        break

if valid:
    binaryNumRev = binaryNum[::-1]

    power = 0
    total = 0

    for i in binaryNumRev:
        total = total + (int(i) * (2 ** power))
        power += 1

    print(f"Binary String: {binaryNum}")
    print(f"Its decimal equivalent: {total}")

else:
    print("Invalid input.")



"""
Enter the binary string: 101101
Binary String: 101101
Its decimal equivalent: 45
"""