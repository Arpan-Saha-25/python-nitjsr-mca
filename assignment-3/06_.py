# Write  a  program,  which  accepts  annual  basic  salary  of  an  employee  and  calculates 
# and displays the Income tax as per the following rules. 
#  If Basic is less than Rs. 1,50,000/-, then Tax = 0 
#  If Basic is from Rs. 1,50,000/- to Rs. 3,00,000/-, then tax is 20% 
#  If Basic is greater than Rs. 3,00,000/-, then tax is 30% 

basic = float(input("Enter annual basic salary: "))

if basic < 150000:
    tax = 0
elif basic <= 300000:
    tax = basic * 20 / 100
else:
    tax = basic * 30 / 100

print("Income Tax =", tax)

# Enter annual basic salary: 170000 
# Income Tax = 34000.0