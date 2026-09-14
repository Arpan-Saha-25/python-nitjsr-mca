# Write a program to read a positive integer X and verify whether: 
# (1) X is divisible by 2. 
# (2) X is divisible by 3. 
# (3) X is divisible by both 2 and 3. 
# (4) X is divisible 2 or 3. 

X = int(input("Enter a positive integer: "))

# divisible by 2
if X % 2 == 0:
    print("X is divisible by 2.")
else:
    print("X is not divisible by 2.")

# divisible by 3
if X % 3 == 0:
    print("X is divisible by 3.")
else:
    print("X is not divisible by 3.")

# divisible by both 2 and 3
if X % 2 == 0 and X % 3 == 0:
    print("X is divisible by both 2 and 3.")
else:
    print("X is not divisible by both 2 and 3.")

# divisible by 2 or 3
if X % 2 == 0 or X % 3 == 0:
    print("X is divisible by 2 or 3.")
else:
    print("X is not divisible by either 2 or 3.")
