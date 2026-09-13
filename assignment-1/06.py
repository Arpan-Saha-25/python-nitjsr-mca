# Write a program to evaluate the expression: 5x^2 + 10x + 5 and print the result. Take x=10, x=20, x=15

x = int(input("Enter the value of x : "))

quad_eqn =  (5*x*x) + (10*x) + 5

print("Value of 5x^2 + 10x + 5 at x =",x,"is", quad_eqn)

"""
output: 

Enter the value of x : 10
Value of 5x^2 + 10x + 5 at x = 10 is 605

Enter the value of x : 20
Value of 5x^2 + 10x + 5 at x = 20 is 2205

Enter the value of x : 15
Value of 5x^2 + 10x + 5 at x = 15 is 1280
"""