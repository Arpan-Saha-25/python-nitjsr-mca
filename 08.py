# A cashier has currency notes of denominations 10, 50 and 100. Take an Input of a number for withdraw amount. Find the total number of currency notes of each denomination the cashier will have to give to the withdrawer.

amount = int(input("Enter the withdrawal amount: "))

notes_100 = amount // 100
# remaining = amount % 100

notes_50 = amount // 50
# remaining = remaining % 50

notes_10 = amount // 10
# remaining = remaining % 10

print(f"Number of 100 notes: {notes_100}")
print(f"Number of 50 notes: {notes_50}")
print(f"Number of 10 notes: {notes_10}")

