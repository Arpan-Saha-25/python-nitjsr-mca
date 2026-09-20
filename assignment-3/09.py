# Write a program in Python to input a sentence with digits also. The program should 
# count the number of uppercase letters, lowercase letters and digits in the sentence.

sentence = input("Enter the string:\n")

upper = lower = digits = 0

for i in sentence:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i.isdigit():
        digits+=1
        
print("The total number of uppercase letters are",upper)
print("The total number of lowercase letters are",lower)
print("The total number of digits are",digits)

# Enter the string:
# This is the assignment number 3.
# The total number of uppercase letters are 1
# The total number of lowercase letters are 24
# The total number of digits are 1