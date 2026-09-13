# Assume Sachin’s basic salary is 10 Lakh. His dearness allowance(DA) is 40% of basic salary, and house rent allowance(HRA) is 20% of basic salary. Write a program to calculate his gross salary.

basic_sal = 1000000
da = 0.4 * basic_sal
hra = 0.2 * basic_sal

gross_sal = basic_sal + da + hra

print("Basic Salary: ", basic_sal)
print("DA:", da)
print("hra:", hra)
print("Gross Salary:", gross_sal)