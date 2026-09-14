# Write  a  program  in  Python  which  inputs  time  in  hours  and  minutes  and  converts  it 
# into seconds.

hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))

seconds = (hours * 60 * 60) + (minutes * 60)

print("Time in seconds:", seconds)



