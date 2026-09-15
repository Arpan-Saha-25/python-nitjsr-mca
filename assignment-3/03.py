# Write a program that accepts three sides of a triangle as input
# and prints whether the triangle is valid or not.

s1 = int(input("Enter the first side: "))
s2 = int(input("Enter the second side: "))
s3 = int(input("Enter the third side: "))

if (s1 + s2 > s3) and (s2 + s3 > s1) and (s3 + s1 > s2):
    print("It is a valid triangle.")
else:
    print("It is not a valid triangle.")

# Enter the first side: 3 
# Enter the second side: 4
# Enter the third side: 5
# It is a valid triangle.

# Enter the first side: 1
# Enter the second side: 2
# Enter the third side: 3
# It is not a valid triangle.