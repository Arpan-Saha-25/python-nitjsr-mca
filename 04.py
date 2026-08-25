# Write a program to swap the contents of two variables using third variable.

num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))

print("Currently, the numbers are",num1,num2)

temp = num1
num1 = num2
num2 = temp

print("After swapping, the numbers are",num1,num2)