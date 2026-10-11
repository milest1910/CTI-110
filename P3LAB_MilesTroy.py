# Troy Miles Jr
# P3LAB
# This might or might not calculate the minimum number of dollars and coins. We'll seeeeeeeeeeeeeeeeeeeeeee

# Get Money amount from user
money = float(input("Enter the amount of money: $"))

# Convert the dollars to cents
cents = int(round(money * 100))

# Calculate dollars
dollars = cents // 100
cents = cents - (dollars * 100)

# Calculate quarters
quarters = cents // 25
cents = cents - (quarters * 25)

# Calc Dimes
dimes = cents // 10
cents = cents - (dimes * 10)

# Calc nickels
nickels = cents // 5
cents = cents - (nickels * 5)

# Remaining cents are PENNIESSSSSSSSSS
pennies = cents

# Display results
if money == 0:
    print("No change")
else:
    if dollars > 0:
        print(dollars, "Dollar" if dollars == 1 else "Dollars")
    if quarters > 0:
        print(quarters, "Quarter" if quarters == 1 else "Quarters")

    if dimes > 0:
        print(dimes, "Dime" if dimes == 1 else "Dimes")

    if nickels > 0:
        print(nickels, "Nickel" if nickels == 1 else "Nickels")

    if pennies > 0:
        print(pennies, "Penny" if pennies == 1 else "Pennies")
