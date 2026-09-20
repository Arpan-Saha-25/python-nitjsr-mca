# A  numeric  palindrome  is  a  number  which  remains  the  same  even  when  you  reverse the
# digits of the given number, e.g., 121, 34543, 6776, etc. 
# Write a Python program to check a given positive number is a numeric palindrome or 
# not. 

# Sample input and output: 
# Input: Enter a positive integer : 12321 
# Output: Yes, 12321 is a numeric palindrome !!!  
# Input: Enter a positive integer : 96596598 
# Output: No, 96596598 is not a numeric palindrome !!!

orgNum = input("Enter a number:\n")
palinNum = (orgNum[::-1])
if orgNum == palinNum:
    print(f"\nYes,{orgNum} is a number palindrome.")
else:
    print(f"\nNo,{orgNum} is not a number palindrome.")
    

# Enter a number:
# 12321

# Yes,12321 is a number palindrome.