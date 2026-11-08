import mytools as mt 
# from mytools import square

print("Square of the given number is" , mt.square(int(input("Enter a number: "))))
print(mt.greet(input("Enter your name: ")))

from myPackage.mathTools import add
print(add(2,3))