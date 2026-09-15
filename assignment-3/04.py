# Write a Python program to check whether a triangle is
# equilateral, isosceles or scalene.
# Hint: Input is the angles of triangles.

a1 = int(input("Enter the first positive angle: "))
a2 = int(input("Enter the second positive angle: "))
a3 = int(input("Enter the third positive angle: "))

if a1 + a2 + a3 != 180:
    print("Invalid triangle.")
elif a1 == a2 and a2 == a3:
    print(">>> Equilateral triangle.")
elif a1 == a2 or a1 == a3 or a2 == a3:
    print(">>> Isosceles triangle.")
else:
    print(">>> Scalene triangle.")

