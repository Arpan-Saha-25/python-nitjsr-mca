# Write a program to find out the highest common factor (HCF) of two given positive 
# integers  n  and  m.  Then  use  HCF  of  n  and  m  to  find  the  least  common  multiple (LCM) of n and m. 

# Sample input and output: 
# Input: Enter n: 10 
# Enter m: 25 
# Output : HCF of 10 and 25 is 5 
# LCM of 10 and 25 is 50 
# Input: Enter n: 20 
# Enter m: 27 
# HCF of 20 and 27 is 1 
# LCM of 20 and 27 is 540

n = int(input("Enter n: "))
m = int(input("Enter m: "))

small = min(n, m)
hcf = 1

for i in range(1, small + 1):
    if n % i == 0 and m % i == 0:
        hcf = i

lcm = (n * m) // hcf

print("HCF of", n, "and", m, "is", hcf)
print("LCM of", n, "and", m, "is", lcm)

# Enter n: 10
# Enter m: 25
# HCF of 10 and 25 is 5
# LCM of 10 and 25 is 50