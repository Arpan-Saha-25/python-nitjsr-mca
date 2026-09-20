# Write a program in Python to calculate the sum of numbers in the range from m to n 
# which are not divisible by 2,3 or 5. where m<n.

m = int(input("Enter the lower range: "))
n = int(input("Enter the upper range: "))

total = 0

if m < n:
    for i in range(m,n+1):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
            total = total  + i
    print(f"The sum numbers in the range from {m} to {n} which are not divisible by 2,3 or 5 is {total}.")
else:
    print("Wrong input.")
    
# Enter the lower range: 30
# Enter the upper range: 35
# The sum numbers in the range from 30 to 35 which are not divisible by 2,3 or 5 is 31.