# Write  a  python  program  to  sum  two  user  input  integers.  However,  if  the  sum  is 
# between x to y it will return True. X and Y is from user. 

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
sum = num1 + num2

while(True):
    X = int(input("\nEnter the lower limit: "))
    Y = int(input("Enter the upper limit: "))

    if X > Y:
        print("Invalid input.")
        continue
    break;

if sum >= X or sum <= Y:
    print("\nIn the range. True")
else:
    print("\nOut of the range. False")
