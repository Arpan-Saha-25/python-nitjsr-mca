
x = int(input("Enter initial number of passengers (X > 10): "))

if x <= 10:
    print("Invalid input! X must be greater than 10.")

else:
    passengers = x

    print("Passengers travelling between S and A:", passengers)

    # At station A
    passengers = passengers - 10 + 12
    print("Passengers travelling between A and B:", passengers)

    # At station B
    passengers = passengers - 10 + 15
    print("Passengers travelling between B and C:", passengers)

    # At station C
    passengers = passengers - 2 + 5
    print("Passengers travelling between C and D:", passengers)

    # At station D
    passengers = passengers - 22 + 28
    print("Passengers travelling between D and E:", passengers)

    # At station E
    passengers = passengers - 7 + 15
    print("Passengers travelling between E and T:", passengers)
