# Write a program for the following problem. 
# Let N be a positive integer (read as the input). Verify that the English calendar  year 
# with  year  number  N  is  a  leap  year  or  not.  Note  that  you  are  not  allwed  to  look  into 
# the  calendar  of  the  year.  Just,  with  the  information  of  year  number  you  need  to 
# answer that the year is a leap or not. 
# Note:  A  year  number  N  is  said  to  be  a  leap  year  in  the  following  cases:  If  N  is  a 
# century year (e.g., 100, 200, 300, ...) and divisible by 400, then N is a leap year. If N 
# is a non-century year and divided by 4, then N is a leap year. In all other cases, N is a 
# non-leap year. 
# Sample input output: 
# Input: Enter a year number : 300 
# Output: The year 300 is not a leap year  
# Input: Enter a year number : 800 
# Output: The year 800 is a leap year  
# Input: Enter a year number : 2019 
# Output: The year 2019 is not a leap year  
# Input: Enter a year number : 2020 
# Output: The year 2020 is a leap year 

n = int(input("Enter a year number: "))

if n % 400 == 0:
    print("The year", n, "is a leap year")
elif n % 100 == 0:
    print("The year", n, "is not a leap year")
elif n % 4 == 0:
    print("The year", n, "is a leap year")
else:
    print("The year", n, "is not a leap year")