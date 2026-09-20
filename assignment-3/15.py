# A  banking  company  sends  a  6-digit  integer  number  as  one-time  password  (OTP)  to 
# its customer mobile for all mobile banking transactions. An integer is a valid OTP if 
# (1) it is of six-digit length and (2) contains the same number of even and odd digits. 
# Further, the OTP does not start with 0. Write a python program to read an integer and 
# verify whether it is a valid OTP or not? 
# Sample input and output: 
# Input : Enter a number : 4564756 
# Output: Invalid OTP  
# Input: Enter a number : 676876 
# Output: Invalid OTP  
# Input: Enter a number : 123456 
# Output: Valid OTP   

n = int(input("Enter a number: "))

if 100000 <= n <= 999999:
    even = 0
    odd = 0
    temp = n

    for i in range(6):
        digit = temp % 10

        if digit % 2 == 0:
            even += 1
        else:
            odd += 1

        temp = temp // 10

    if even == odd:
        print("Valid OTP")
    else:
        print("Invalid OTP")
else:
    print("Invalid OTP")