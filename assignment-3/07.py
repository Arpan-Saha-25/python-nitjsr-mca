# Write  a  program  in  Python  to  print  odd  numbers  from  1  to  10  except  7.  (Hint:  use 
# continue statement) 

for i in range(1, 11):
    if i == 7:
        continue

    if i % 2 != 0:
        print(i)

