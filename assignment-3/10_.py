# Write a program to find the factorial of a given positive integer n. The factorial of a 
# number is the product of all the integers from 1 to n. 
# i.e., n! = n * (n-1) * .... * 1. 
# Sample input and output 
# Enter the value of n : 10 
# Output: (10 !) = 3628800 

n = int(input("Enter a number: "))
temp = n
fact = 1

while(n > 0):
    fact = fact * n
    n-=1
    
print(f"{temp}! =", fact)

# Enter a number: 10
# 10! = 3628800